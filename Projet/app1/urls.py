from django.urls import path
from .views import page_authentification
from .views import ajouter_patient
from .views import liste_patients
from .views import ajouter_medecin
from .views import liste_medecins

urlpatterns = [ 
    path('',page_authentification,name='page_authentification'),          
    path('ajouter_patient/',ajouter_patient,name='ajouter_patient'),
    path('liste_patients/',liste_patients, name ='liste_patients'),
    path('ajouter_medecin/',ajouter_medecin, name='ajouter_medecin'),
    path('liste_medecins/',liste_medecins, name='liste_medecins'),
]

