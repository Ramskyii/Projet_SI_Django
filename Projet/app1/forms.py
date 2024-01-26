from django import forms
from .models import Patient
from .models import Medecin

class PatientForm(forms.ModelForm) :
    class Meta:
        model = Patient
        fields = '__all__'


class MedecinForm(forms.ModelForm) :
    class Meta : 
        model = Medecin
        fields = '__all__'

