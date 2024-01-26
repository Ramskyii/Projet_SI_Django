from django.urls import path
from .views import page_authentification
from .views import ajouter_patient
from .views import liste_patients

urlpatterns = [ 
    path('',page_authentification,name='page_authentification'),          
    path('ajouter_patient/',ajouter_patient,name='ajouter_patient'),
    path('liste_patients/',liste_patients, name ='liste_patients'),
]

