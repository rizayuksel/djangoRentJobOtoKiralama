from django.shortcuts import render, HttpResponse, redirect
from .models import Rent
from Autos.models import Autos
from .forms import RentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def rentACar(request):      
    form = RentForm(request.POST or None)
    #Veri Tabanına Kaydetme İşlemleri
    if form.is_valid():
        rent = form.save(commit=False)
        rent.renter = request.user
        rent.save()
        messages.info(request,"Rezervasyon işlemi başarıyla tamamlandı. Şubemizde ödemenizi yaptıktan sonra aracınızı alabilirsiniz. İyi günler dileriz.")
        return redirect("index")
    return render(request, "rentACar.html", {"form":form})

