from django.contrib import admin
from django.urls import path
from . import views

app_name = "Autos" #Redirect için gerek

urlpatterns = [
    path('allcars/', views.allCars, name="allcars"), #Araçlar
    path('audi/', views.audi, name="audi"), #Audi
    path('bmw/', views.bmw, name="bmw"), #Bmw
    path('mazda/', views.mazda, name="mazda"), #Mazda
    path('volkswagen/', views.volkswagen, name="volkswagen"), #Volkswagen
    path('volvo/', views.volvo, name="volvo"), #Volvo
    path('auto/<int:id>', views.detail, name="detail"), #Detay
    #
    # path('rentacar/', views.rentACar, name="rentacar"),
    # path('search/', views.search, name="search"),
    #
]