from django.urls import path
from .views import page_authentification
from .views import ajouter_patient
from .views import liste_patients
from .views import ajouter_medecin
from .views import liste_medecins
from .views import acceuil
from .views import ajouter_rdv
from .views import liste_rdv
from .views import index
 

urlpatterns = [ 
    path('',page_authentification,name='page_authentification'),          
    path('ajouter_patient/',ajouter_patient,name='ajouter_patient'),
    path('liste_patients/',liste_patients, name ='liste_patients'),
    path('ajouter_medecin/',ajouter_medecin, name='ajouter_medecin'),
    path('liste_medecins/',liste_medecins, name='liste_medecins'),
    path('acceuil/',acceuil,name='acceuil'),
    path('ajouter_rdv',ajouter_rdv,name='ajouter_rdv'),
    path('liste_rdv/',liste_rdv,name='liste_rdv'),
    path('index/',index,name='Home'),
]

