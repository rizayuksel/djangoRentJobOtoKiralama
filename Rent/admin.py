from django.contrib import admin
from .models import Rent

@admin.register(Rent)
class RentAdmin(admin.ModelAdmin): #Admin panelini özelleştirmek için
    list_display = ["renter","rentedCar","rentalDate","transactionDate","totalDays"] #Admin panelinde göstermek istediğimiz bilgiler
    search_fields = ["renter"] #Admin paneline arama çubuğu geldi
    list_filter = ["renter","rentedCar","rentalDate"] #Admin panelinde filtre oluşturduk
    #list_max_show_all = 10
    class Meta:
        model = Rent #AutosAdmin'le Autos'u bağladık

