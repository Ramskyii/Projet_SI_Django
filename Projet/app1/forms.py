from django import forms
from .models import Patient
from .models import Medecin
from .models import RendezVous
from .models import Dossier

class PatientForm(forms.ModelForm) :
    class Meta:
        model = Patient
        fields = '__all__'


class MedecinForm(forms.ModelForm) :
    class Meta : 
        model = Medecin
        fields = '__all__'

class DossierForm(forms.ModelForm):
    class Meta:
        model = Dossier
        fields = '__all__'


class RendezVousForm(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = '__all__'
        widgets = {
            'Date_rdv': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(RendezVousForm, self).__init__(*args, **kwargs)
    
        medecins = Medecin.objects.all()
        self.fields['Num_Medecin'].queryset = medecins
        self.fields['Num_Medecin'].label_from_instance = lambda obj: f'{obj.Nom_M} {obj.Prenom_M} {obj.specialite}'

        patients = Patient.objects.all()
        self.fields['Num_Patient'].queryset = patients
        self.fields['Num_Patient'].label_from_instance = lambda obj: f'{obj.Nom_P} {obj.Prenom_P}'

