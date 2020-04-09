from django.db import models

class Autos(models.Model): #otomobiller tablosu
    title = models.CharField(max_length=100, verbose_name="Başlık")
    trademark = models.CharField(max_length=50, verbose_name="Marka")
    model = models.CharField(max_length=50, verbose_name="Model")
    year = models.CharField(max_length=10, verbose_name="Yıl")
    gear = models.CharField(max_length=20, verbose_name="Vites")
    fuel = models.CharField(max_length=20, verbose_name="Yakıt")
    carClass = models.CharField(max_length=30, verbose_name="Sınıf")
    horsePower = models.CharField(max_length=5, verbose_name="Beygir Gücü")
    baggageVolume = models.CharField(max_length=15,verbose_name="Bagaj Hacmi")
    price = models.IntegerField(verbose_name="Günlük Ücret")
    autoImage = models.FileField(blank=True, null=True, verbose_name="Otomobilin Resmini Ekleyin")
    def __str__(self):
        return self.title
