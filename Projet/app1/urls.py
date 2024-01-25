from django.urls import path
from .views import affiche_rdv

urlpatterns = [ ...,
               
    path('rdv', affiche_rdv ,name= 'liste_rdv'),

]

