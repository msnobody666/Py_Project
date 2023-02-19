# Create your views here. 
from django.http import HttpRequest

from datetime import datetime, date 

class FormularPojistence: 
    def __init__(self, request:HttpRequest): 
        self.jmeno = request.POST.get("jmeno") 
        self.jmeno_error = None
        self.prijmeni = request.POST.get("prijmeni") 
        self.prijmeni_error = None
        self.email = request.POST.get("email") 
        self.telefon = request.POST.get("telefon")
        self.adresa = request.POST.get("adresa") 
        self.mesto = request.POST.get("mesto")
        self.psc = request.POST.get("psc") 

# VALIDACE UZIVATELSKEHO VSTUPU 
# PRO POJISTENCE 

    def zvaliduj(self): # vráti True pokial je tam chyba
        if self.jmeno.isspace() or self.jmeno == "": 
            self.jmeno_error = "Vyplňte jméno."
        elif self.jmeno.isnumeric(): 
            self.jmeno_error = "Jméno nesmí obsahovat číslice." 
        
        if self.prijmeni.isspace() or self.prijmeni == "": 
            self.prijmeni_error = "Vyplňte příjmení."
        elif self.prijmeni.isnumeric(): 
            self.prijmeni_error = "Příjmení nesmí obsahovat číslice." 
        
        return self.jmeno_error is not None or self.prijmeni_error is not None

# VALIDACE UZIVATELSKEHO VSTUPU 
# PRO POJISTENI  


class FormularPojisteni: 


    def __init__(self, request:HttpRequest):
        self.typ = request.POST.get("typ") 
        self.castka = request.POST.get("castka")
        self.castka_error = None
        self.predmet = request.POST.get("predmet")
        self.predmet_error = None
        self.platnost_od = request.POST.get("platnost_od")
        self.platnost_od_error = None
        self.platnost_do = request.POST.get("platnost_do") 
        self.platnost_do_error = None


    def zvaliduj(self): # vráti True pokial je tam chyba
        if not self.castka.lstrip("-").isdigit():  
        # https://stackoverflow.com/questions/28279732/how-to-type-negative-number-with-isdigit
            self.castka_error = "Zadejte číslo." 
        else:
            self.castka = int(self.castka)
            if self.castka <= 0:
                self.castka_error = "Zadejte číslo větší než 0." 
             
        
        if self.predmet.isspace() or self.predmet == "" or self.predmet.isnumeric(): 
            self.predmet_error = "Vyplňte předmět." 
        
        
        if self.platnost_od == "":  
            self.platnost_od_error = "Zvolte začátek platnosti." 
        else: 
            self.platnost_od = parsuj_datum(self.platnost_od) 
            if self.platnost_od < date.today(): 
                self.platnost_od_error = "Datum platnosti nesmí být zvolen před dnešním datem."  

        if self.platnost_do == "":  
            self.platnost_do_error = "Zvolte konec platnosti." 
        else: 
            self.platnost_do = parsuj_datum(self.platnost_do)  
            if self.platnost_do<=date.today(): 
                self.platnost_do_error = "Konec platnosti nesmí být zvolen před dnešním datem."   


        if self.platnost_do_error is None and self.platnost_od_error is None and self.platnost_do<=self.platnost_od: 
            self.platnost_do_error = "Konec platnosti musí nesmí být zvolen před začátkem platnosti."         
        
        return self.castka_error is not None or self.predmet_error is not None or self.platnost_od_error is not None or self.platnost_do_error is not None 

   
def parsuj_datum(datum): 
    return datetime.strptime(datum,'%Y-%m-%d').date()

