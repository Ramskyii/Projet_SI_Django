from django.urls import path
from . import views

urlpatterns = [ 
              
    path('RendezVous/',views.affiche_rdv,name='RendezVous')

]

