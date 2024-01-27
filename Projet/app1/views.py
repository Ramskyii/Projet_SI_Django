from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientForm
from .models import Patient
from .forms import MedecinForm
from .models import Medecin
from .forms import RendezVousForm
from .models import RendezVous


def liste_patients(request):

    query = request.GET.get('q')
    patients = Patient.objects.all()
    if query:
        patients = patients.filter(Nom_P__icontains=query)

    return render(request, 'liste_patients.html', {'patients': patients, 'query': query})


def prefillPatient(request, pk):
    patient = Patient.objects.get(Num_P=pk)
    form = PatientForm(instance=patient)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('liste_patients')
        
    request.session['patient_to_update'] = pk

    context = {'form': form}
    return render(request, 'ajouter_patient.html', context) 



def liste_medecins(request): 
    medecins = Medecin.objects.all()
    return render(request, 'liste_medecins.html', {'medecins': medecins})


def page_authentification(request):
    return render(request, 'page_authentification.html')



def ajouter_patient(request):
    patient_to_update = request.session.pop('patient_to_update', None)

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            if patient_to_update:
                patient = Patient.objects.get(Num_P= patient_to_update)
                form = PatientForm(request.POST, instance=patient)
            form.save()
            print("Patient ajouté ou mis à jour avec succès!")
            return redirect('liste_patients')  
        
    else:
        form = PatientForm()

    return render(request, 'liste_patients.html', {'form': form})



def supprimer_patient(request, pk):
    patient = Patient.objects.get(Num_P=pk)
    patient.delete()
    return redirect('liste_patients')




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

def index(request):
    return render(request, 'index.html')


def ajouter_rdv(request):
    rendezvous_to_update = request.session.pop('rendezvous_to_update', None)

    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            if rendezvous_to_update:
                rendezvous = RendezVous.objects.get(Num_rdv=rendezvous_to_update)
                form = RendezVousForm(request.POST, instance=rendezvous)
            form.save()
            print("Rendez-vous ajouté ou mis à jour avec succès!")
            return redirect('liste_rdv')
        else:
            print("Formulaire invalide. Erreurs :", form.errors)
    else:
        form = RendezVousForm()

    return render(request, 'ajouter_rdv.html', {'form': form})



def liste_rdv(request):
    query = request.GET.get('q')
    rdvs= RendezVous.objects.all()

    if query:
        rdvs = rdvs.filter(Num_Patient__Nom_P__icontains=query)

    return render(request,'liste_rdv.html',{'rdvs': rdvs , 'query': query})

def prefillRendezVous(request, pk):
    rendezvous = RendezVous.objects.get(Num_rdv=pk)
    form = RendezVousForm(instance=rendezvous)

    if request.method == 'POST':
        form = RendezVousForm(request.POST, instance=rendezvous)
        if form.is_valid():
            form.save()
            return redirect('liste_rdv')
        
    request.session['rendezvous_to_update'] = pk

    context = {'form': form}
    return render(request, 'ajouter_rdv.html', context)


def supprimer_rdv(request,pk):
    rendezvous = get_object_or_404(RendezVous,Num_rdv = pk)
    rendezvous.delete()
    return redirect('liste_rdv')
