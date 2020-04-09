from django.contrib import admin
from .models import Autos #models'den Autos tablosunu ekledik

@admin.register(Autos)
class AutosAdmin(admin.ModelAdmin): #Admin panelini özelleştirmek için
    list_display = ["title","year","gear","fuel","carClass","price"] #Admin panelinde göstermek istediğimiz bilgiler
    search_fields = ["title"] #Admin paneline arama çubuğu geldi
    list_filter = ["trademark","year","gear","fuel","carClass","price"] #Admin panelinde filtre oluşturduk
    #list_max_show_all = 10
    class Meta:
        model = Autos #AutosAdmin'le Autos'u bağladık

