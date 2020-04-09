"""RentJobProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from Autos import views
#from Rent import views
from django.conf import settings #File Upload
from django.conf.urls.static import static #File Upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"), #Ana sayfa
    path('office/', views.office, name="office"), #Şubelerimiz
    path('history/', views.history, name="history"), #Tarihçemiz
    path('autos/', include("Autos.urls")), #Autos uygulaması altındaki urls'e gider. Bu url'ler sitede rentjob.com/autos/"urlismi" olarak görülür.
    path('user/', include("User.urls")), #User uygulaması altındaki urls'e gider. Bu url'ler sitede rentjob.com/user/"urlismi" olarak görülür.
    path('rent/', include("Rent.urls")) #Rent uygulaması altındaki urls'e gider. Bu url'ler sitede rentjob.com/rent/"urlismi" olarak görülür.
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
 #File Upload