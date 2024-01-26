from django.shortcuts import render, redirect
from .forms import PatientForm
from .models import Patient
from .forms import MedecinForm
from .models import Medecin
from .forms import RendezVousForm
from .models import RendezVous


def liste_patients(request):
    patients = Patient.objects.all()
    return render(request, 'liste_patients.html', {'patients': patients})


def liste_medecins(request): 
    medecins = Medecin.objects.all()
    return render(request, 'liste_medecins.html', {'medecins': medecins})


def page_authentification(request):
    return render(request, 'page_authentification.html')



def ajouter_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ajouter_patient')  
    else:
        form = PatientForm()

    return render(request, 'ajouter_patient.html', {'form': form})



def ajouter_medecin(request):
    if request.method == 'POST':
        form = MedecinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ajouter_medecin')
    else:
        form = MedecinForm()

    return render(request, 'ajouter_medecin.html', {'form': form})


def acceuil(request):
    return render(request,'acceuil.html')



def ajouter_rdv(request):
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            form.save()
            print("Rendez-vous ajouté avec succès!")
            return redirect('liste_rdv')
        else:
            print("Formulaire invalide. Erreurs :", form.errors)
    else:
        form = RendezVousForm()

    return render(request, 'ajouter_rdv.html', {'form': form})



def liste_rdv(request):
    rdvs= RendezVous.objects.all()
    return render(request,'liste_rdv.html',{'rdvs': rdvs})