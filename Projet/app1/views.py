from django.shortcuts import render
from .models import RendezVous


def affiche_rdv(request):
    rendezvous = RendezVous.objects.all()
    return render(request, 'index.html', {'rendezvous': rendezvous})

