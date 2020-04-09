from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Autos

# Create your views here.
def index(request):
    return render(request,"index.html")

def office(request):
    return render(request,"office.html")

def history(request):
    return render(request,"history.html")

def allCars(request):
    keyword = request.GET.get("keyword")#arama yapmak için
    if keyword:
        allCars = Autos.objects.filter(title__contains = keyword)
        return render(request, "allcars.html", {"allCars":allCars})
    allCars = Autos.objects.all() #Autos veri tabanındaki tüm verileri sözlük yapısıyla aldık
    return render(request,"allcars.html",{"allCars":allCars})


def detail(request,id):
    auto =get_object_or_404(Autos, id = id)
    return render(request, "detail.html",{"auto":auto})

def audi(request):
    allCars = Autos.objects.filter(title__contains = "Audi")
    return render(request,"audi.html",{"allCars":allCars})

def bmw(request):
    allCars = Autos.objects.filter(title__contains = "Bmw")
    return render(request,"bmw.html",{"allCars":allCars})

def mazda(request):
    allCars = Autos.objects.filter(title__contains = "Mazda")
    return render(request,"mazda.html",{"allCars":allCars})

def volkswagen(request):
    allCars = Autos.objects.filter(title__contains = "Volkswagen")
    return render(request,"volkswagen.html",{"allCars":allCars})

def volvo(request):
    allCars = Autos.objects.filter(title__contains = "Volvo")
    return render(request,"volvo.html",{"allCars":allCars})

