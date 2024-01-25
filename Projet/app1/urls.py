from django.urls import path
from .views import affiche_rdv

urlpatterns = [ 
              
    path('RendezVous/',affiche_rdv,name='RendezVous'),

]

