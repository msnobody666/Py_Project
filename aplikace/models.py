from django.db import models
from .validace import FormularPojistence, FormularPojisteni

# Create your models here.

class Pojistenec(models.Model):
    # "id" je implicitni atribut, takze ho nemusime specifikovat v databazi/tride jako primary key, kedze ho tam Django dáva samo 
    jmeno = models.CharField(max_length=20)
    prijmeni = models.CharField(max_length=20) 
    email = models.CharField(max_length=30) 
    telefon = models.CharField(max_length=20) 
    adresa = models.CharField(max_length=20) 
    mesto = models.CharField(max_length=20) 
    psc = models.CharField(max_length=6)
        

class Pojisteni(models.Model):
    # "id" je implicitni atribut
    typ = models.CharField(max_length=20)
    pojistenec = models.ForeignKey(Pojistenec, on_delete=models.CASCADE) # pojistenec je v tomto pripade číslo/ID 
    castka = models.PositiveIntegerField() 
    predmet = models.CharField(max_length=20) 
    platnost_od = models.DateField()  
    platnost_do = models.DateField() 

class DB:
    
    def loadAllPojistenci(self):
        return Pojistenec.objects.all()

    def loadPojistenec(self, pojistenec_id: int):
        return Pojistenec.objects.get(id = pojistenec_id)
    
    def createPojistenec(self, formular: FormularPojistence):     
    # FormularPojistenec = třída/typ pro promennou formular, t.j. na promennou formular v téhle metode muzeme volat funkce a pouzivat atributy ktore su definovane v tride FormularPojistenec, to same formular Pojiteni
        pojistenec = Pojistenec(
            jmeno = formular.jmeno,
            prijmeni = formular.prijmeni,
            email = formular.email,
            telefon = formular.telefon,
            adresa = formular.adresa,
            mesto = formular.mesto,
            psc = formular.psc,
        )
        pojistenec.save()
        return pojistenec.id

    def updatePojistenec(self, pojistenec_id, formular):
        Pojistenec(
            id = pojistenec_id,
            jmeno = formular.jmeno,
            prijmeni = formular.prijmeni,
            email = formular.email,
            telefon = formular.telefon,
            adresa = formular.adresa,
            mesto = formular.mesto,
            psc = formular.psc,
        ).save()

    def deletePojistenec(self, pojistenec_id: int):
        # https://stackoverflow.com/questions/3805958/how-to-delete-a-record-in-django-models
        Pojistenec.objects.get(id = pojistenec_id).delete()


    def loadAllPojisteni(self, pojistenec_id: int):
        return Pojisteni.objects.filter(pojistenec=pojistenec_id) 
        # https://stackoverflow.com/questions/2367747/django-get-foreign-key-objects-in-single-query

    def loadPojisteni(self, pojistenec_id: int, pojisteni_id: int):
        return Pojisteni.objects.get(id = pojisteni_id) 

    def updatePojisteni(self, pojistenec_id: int, pojisteni_id, formular: FormularPojisteni):    
        Pojisteni( 
            id = pojisteni_id, 
            pojistenec_id = pojistenec_id,
            typ = formular.typ,
            castka = formular.castka,
            predmet = formular.predmet,
            platnost_od = formular.platnost_od,
            platnost_do = formular.platnost_do,
        ).save()  


    def createPojisteni(self, pojistenec_id, formular): 

        pojistenec = self.loadPojistenec(pojistenec_id)
        pojisteni = pojistenec.pojisteni_set.create(
            typ = formular.typ,
            castka = formular.castka,
            predmet = formular.predmet,
            platnost_od = formular.platnost_od,
            platnost_do = formular.platnost_do, 
            pojistenec = pojistenec_id,
        )
        return pojisteni.id


    def deletePojisteni(self, pojistenec_id: int, pojisteni_id: int):
        Pojisteni.objects.get(id = pojisteni_id).delete()




