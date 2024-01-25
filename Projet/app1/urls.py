from django.urls import path
from .views import affiche_rdv
from .views import page_authentification

urlpatterns = [ 
    path('',page_authentification,name='page_authentification'),          
    path('RendezVous/',affiche_rdv,name='RendezVous'),

]

