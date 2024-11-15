from django.urls import path
from .views import *

urlpatterns = [
    path('inscription.html',inscription,name='inscription'),
    path('logout',logoutt,name='logout'),
    path('connexion.html',loginn,name="connexion"),
    path('profil.html/',profil,name="profil"),
]