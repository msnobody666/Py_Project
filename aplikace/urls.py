"""finalni_projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [

    path('pojistenec/', views.vypis_vsech_pojistencu),
    path('pojistenec/novy', views.vytvor_pojistence),
    path('pojistenec/<int:pojistenec_id>', views.zobraz_pojistence),
    path('pojistenec/<int:pojistenec_id>/editace', views.edituj_pojistence),
    path('pojistenec/<int:pojistenec_id>/odstraneni', views.smaz_pojistence),
    
    path('pojistenec/<int:pojistenec_id>/pojisteni/novy', views.vytvor_pojisteni),
    path('pojistenec/<int:pojistenec_id>/pojisteni/<int:pojisteni_id>', views.zobraz_pojisteni),
    path('pojistenec/<int:pojistenec_id>/pojisteni/<int:pojisteni_id>/editace', views.edituj_pojisteni), 
    path('pojistenec/<int:pojistenec_id>/pojisteni/<int:pojisteni_id>/odstraneni', views.smaz_pojisteni), 
]
