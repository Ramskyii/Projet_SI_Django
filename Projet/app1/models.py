from typing import Any
from django.db import models


class Patient(models.Model) : 
    Num_P = models.AutoField(primary_key=True)
    Nom_P = models.CharField(max_length = 50)
    Prenom_P = models.CharField(max_length = 50)
    DateNaissance = models.DateField()
    Telephone_P = models.CharField(max_length = 10, help_text = 'Entrez un numero de telephone valable svp')
    Adresse_P = models.CharField(max_length = 50)
    choix_genre = [
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    ]
    Genre = models.CharField(max_length = 1,choices = choix_genre)
    def delete(self):
        return super().delete()  
    
    def rendezvous_set(self):
        return RendezVous.objects.filter(Num_p=self)

class Medecin(models.Model) : 
    Num_M = models.AutoField(primary_key=True)
    Nom_M = models.CharField(max_length = 50)
    Prenom_M = models.CharField(max_length = 50)
    Telephone_M = models.CharField(max_length = 10, help_text = 'Entrez un numero de telephone valable svp')
    choix_speciailte = [
        ('Cardiologist','Cardiologist'),
        ('Neurologist','Neurologist'),
        ('Urologist','Urologist'),
        ('Rheumatologist','Rheumatologist'),
        ('Otolaryngologist','Otolaryngologist'),
    ]
    specialite = models.CharField(max_length = 50, choices = choix_speciailte)
    
    def delete(self):
        return super().delete()  
    
class RendezVous(models.Model) : 
    Num_rdv = models.AutoField(primary_key=True)
    Date_rdv = models.DateTimeField()
    salle = models.ForeignKey('Salle', on_delete=models.CASCADE)
    Num_Patient = models.ForeignKey(Patient,on_delete = models.CASCADE)
    Num_Medecin = models.ForeignKey(Medecin,on_delete = models.CASCADE)
    choix_departement = [
        ('Card','Cardiology'),
        ('Neuro','Neurology'),
        ('Urol','Urology'),
        ('Rheum','Rheumatology'),
        ('ENT','Ear, Nose, and Throat'),
    ]

    departement = models.CharField(max_length = 50, choices = choix_departement)

    def delete(self):
        return super().delete()  
    

class Dossier(models.Model) : 
    Num_D = models.AutoField(primary_key=True)
    Derniere_modif = models.DateTimeField(auto_now=True)
    Num_Patient = models.OneToOneField(Patient,on_delete = models.CASCADE)
    
    def get_diagnostics(self):
        return Diagnostic.objects.filter(Num_rendezvous__Num_Patient=self.Num_Patient)

class Diagnostic(models.Model) : 
    Num_Diag = models.AutoField(primary_key=True)
    Desc_diag = models.CharField(max_length = 1000)
    Num_rendezvous = models.OneToOneField(RendezVous,on_delete = models.CASCADE)
    

class Ordonnance(models.Model) : 
    Num_ord = models.AutoField(primary_key=True)
    Designation = models.CharField(max_length = 1000)
    Num_diagnostic = models.OneToOneField(Diagnostic,on_delete = models.CASCADE)
    Medicaments = models.ManyToManyField('Medicament')
    

class Medicament(models.Model) : 
    Code_Medic = models.AutoField(primary_key=True)
    Nom_Medic = models.CharField(max_length = 50)

class Salle (models.Model) : 
    Num_salle = models.AutoField(primary_key=True)
    choix_de_type = [
        ('consultation', 'salle de consultation'),
        ('operation', 'salle d\'opération'),
    ]
    type_salle = models.CharField(max_length = 50, choices = choix_de_type)