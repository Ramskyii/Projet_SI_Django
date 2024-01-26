from django.shortcuts import render, redirect
from .forms import PatientForm
from .models import Patient


def liste_patients(request):
    patients = Patient.objects.all()
    return render(request, 'liste_patients.html', {'patients': patients})

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


