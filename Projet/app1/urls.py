from django.urls import path
from .views import page_authentification
from .views import ajouter_patient
from .views import liste_patients
from .views import ajouter_medecin
from .views import liste_medecins
from .views import ajouter_rdv
from .views import liste_rdv
from .views import index
from .views import prefillRendezVous
from .views import supprimer_rdv
from .views import prefillPatient
from .views import supprimer_patient
from .views import supprimer_medecin
from .views import prefillMedecin
from .views import Dossier_medical
from .views import Diagnostic
from .views import ajouter_diagnostic
from .views import liste_diagnostics
from .views import afficher_diagnostic_rendezvous
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns = [ 
    path('',page_authentification,name='page_authentification'),          
    path('ajouter_patient/',ajouter_patient,name='ajouter_patient'),
    path('liste_patients/',liste_patients, name ='liste_patients'),
    path('ajouter_medecin/', ajouter_medecin, name='ajouter_medecin'),
    path('diagnostic/', ajouter_diagnostic, name='ajouter_diagnostic'),
    path('liste_medecins/',liste_medecins, name='liste_medecins'),
    path('ajouter_rdv',ajouter_rdv,name='ajouter_rdv'),
    path('liste_rdv/',liste_rdv,name='liste_rdv'),
    path('index/',index,name='Home'),
    path('prefill_rendezVous/<int:pk>/',prefillRendezVous,name='prefill_rendezVous'),
    path('supprimer_rdv/<int:pk>/',supprimer_rdv,name='supprimer_rdv'),
    path('prefill_patient/<int:pk>/', prefillPatient, name='prefill_patient'),
    path('supprimer_patient/<int:pk>/',supprimer_patient,name='supprimer_patient'),
    path('dossier_medical/<int:patient_id>/', Dossier_medical, name='Dossier_medical'),
    path('supprimer_medecin/<int:pk>/',supprimer_medecin,name='supprimer_medecin'),
    path('prefillMedecin/<int:pk>/', prefillMedecin, name='prefillMedecin'),
    path('liste_diagnostics/', liste_diagnostics, name='liste_diagnostic'),
    path('afficher_diagnostic_rendezvous/<int:rendezvous_id>/', afficher_diagnostic_rendezvous, name='afficher_diagnostic_rendezvous'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

