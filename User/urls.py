from django.contrib import admin
from django.urls import path
from . import views

app_name = "User"

urlpatterns = [
    path('register/', views.register, name="register"), #Kayıt Ol
    path('login/', views.loginUser, name="login"), #Giriş Yap
    path('logout/', views.logoutUser, name="logout"), #Çıkış Yap
    path('profile/', views.userProfile, name="profile") #Profil
]