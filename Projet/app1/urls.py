from django.urls import path
from . import views

urlpatterns = [ ...,
               
    path('rdv',views.affiche_rdv)
    
]

