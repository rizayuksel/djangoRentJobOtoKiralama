from django.db import models

class Rent(models.Model):
    renter = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name="Kiralayan Kullanıcı")
    rentedCar = models.ForeignKey("Autos.Autos", on_delete = models.CASCADE, verbose_name="Kiralanan Otomobil")
    rentalDate = models.DateField(verbose_name="Kiralanma Tarihi (Gün/Ay/Yıl)")
    totalDays = models.IntegerField(verbose_name="Gün Sayısı")
    transactionDate = models.DateTimeField(auto_now_add=True, verbose_name="İşlem Tarihi")