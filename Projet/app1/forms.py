from django import forms
from .models import Patient
from .models import Medecin
from .models import RendezVous
from .models import Dossier
from .models import Salle
from .models import Diagnostic



class CustomSalleWidget(forms.Select):
    def render_option(self, selected_choices, option_value, option_label):
       
        option_label = Salle.objects.get(Num_Salle=option_value).type_salle
        return super().render_option(selected_choices, option_value, option_label)  

class PatientForm(forms.ModelForm) :
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'DateNaissance': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
    


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

        salles = Salle.objects.all()
        self.fields['salle'].widget = CustomSalleWidget()
        self.fields['salle'].queryset = salles
        self.fields['salle'].label_from_instance = lambda obj: f'{obj.Num_salle} {obj.type_salle}'
        medecins = Medecin.objects.all()
        self.fields['Num_Medecin'].queryset = medecins
        self.fields['Num_Medecin'].label_from_instance = lambda obj: f'{obj.Nom_M} {obj.Prenom_M} {obj.specialite}'

        patients = Patient.objects.all()
        self.fields['Num_Patient'].queryset = patients
        self.fields['Num_Patient'].label_from_instance = lambda obj: f'{obj.Nom_P} {obj.Prenom_P}'


class DiagnosticForm(forms.ModelForm):
    class Meta:
        model = Diagnostic
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DiagnosticForm, self).__init__(*args, **kwargs)

        rendvs = RendezVous.objects.all()
        self.fields['Num_rendezvous'].widget = CustomSalleWidget()
        self.fields['Num_rendezvous'].queryset = rendvs
        self.fields['Num_rendezvous'].label_from_instance = lambda obj: f'{obj.Num_rdv} {obj.Date_rdv} '

