# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpRequest

from .models import DB 
from .validace import FormularPojistence, FormularPojisteni 

db = DB()

def vypis_vsech_pojistencu(request: "HttpRequest"):
    return render(request, "pojistenec/list.html", dict(
        operace=request.GET.get("operace"),
        vsichni_pojistenci=db.loadAllPojistenci()
    )) 

def vytvor_pojistence(request: "HttpRequest"):
    if request.method == "GET":
        return render(request, "pojistenec/form.html")

    if request.method == "POST":
        formular = FormularPojistence(request) 
        obsahuje_chybu = formular.zvaliduj() 
        if obsahuje_chybu: 
            return render(request, "pojistenec/form.html", dict(formular=formular))
        else: 
            id = db.createPojistenec(formular)
            return redirect('/pojistenec/{}?operace=editace_pojistence'.format(id))


def zobraz_pojistence(request: "HttpRequest", pojistenec_id):
    return render(request, "pojistenec/profil.html", dict(
        pojistenec=db.loadPojistenec(pojistenec_id),
        vsechny_pojisteni=db.loadAllPojisteni(pojistenec_id),
        operace=request.GET.get("operace"),
    ))

def edituj_pojistence(request: "HttpRequest", pojistenec_id): 
    if request.method == "GET":
        pojistenec = db.loadPojistenec(pojistenec_id)
        return render(request, "pojistenec/form.html", dict(
            formular=pojistenec)) 

    if request.method == "POST":
        formular = FormularPojistence(request) 
        obsahuje_chybu = formular.zvaliduj() 
        if obsahuje_chybu: 
            return render(request, "pojistenec/form.html", dict(formular=formular))
        else: 
            db.updatePojistenec(pojistenec_id, formular) 
            return redirect('/pojistenec/{}?operace=editace_pojistence'.format(pojistenec_id)) 


def smaz_pojistence(request: "HttpRequest", pojistenec_id):
    # delete FROM tabulky WHERE pojisteni_id = to co chceme zmazat
    db.deletePojistenec(pojistenec_id)
    return redirect('/pojistenec?operace=odstraneni_pojistence')


def vytvor_pojisteni(request: "HttpRequest", pojistenec_id):
    if request.method == "GET": 
        return render(request, "pojisteni/form.html") 

    if request.method == "POST": 
        formular = FormularPojisteni(request)
        obsahuje_chybu = formular.zvaliduj()
        if obsahuje_chybu: 
            return render(request, "pojisteni/form.html", dict(formular=formular)) 
        else:  
            id = db.createPojisteni(pojistenec_id,formular)
            return redirect('/pojistenec/{}/pojisteni/{}?operace=editace_pojisteni'.format(pojistenec_id, id))


def zobraz_pojisteni(request: "HttpRequest", pojistenec_id, pojisteni_id):
    pojisteni=db.loadPojisteni(pojistenec_id, pojisteni_id)
    return render(request, "pojisteni/detail.html", dict(
        pojistenec=db.loadPojistenec(pojistenec_id),
        pojisteni=db.loadPojisteni(pojistenec_id, pojisteni_id),
        operace=request.GET.get("operace"),
    ))

def edituj_pojisteni(request: "HttpRequest", pojistenec_id, pojisteni_id):
    
    if request.method == "GET": 
        pojisteni = db.loadPojisteni(pojistenec_id, pojisteni_id) 
        return render(request, "pojisteni/form.html", dict(formular=pojisteni)) 

    if request.method == "POST": 
        formular = FormularPojisteni(request)
        obsahuje_chybu = formular.zvaliduj() 
        if obsahuje_chybu: 
            return render(request, "pojisteni/form.html", dict(formular=formular))
        else: 
            db.updatePojisteni(pojistenec_id, pojisteni_id, formular)  
            return redirect('/pojistenec/{}/pojisteni/{}?operace=editace_pojisteni'.format(pojistenec_id, pojisteni_id))
 

def smaz_pojisteni(request: "HttpRequest", pojistenec_id, pojisteni_id):
    # delete FROM tabulky WHERE pojisteni_id = to co chceme zmazat
        db.deletePojisteni(pojistenec_id, pojisteni_id) 
        return redirect('/pojistenec/{}?operace=odstraneni_pojisteni'.format(pojistenec_id))

