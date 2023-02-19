from django.contrib import admin

# Register your models here.
from .models import Pojistenec, Pojisteni

admin.site.register(Pojistenec)
admin.site.register(Pojisteni)