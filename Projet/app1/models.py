from django.db import models

class Patient(models.Model) : 
    Nom_P = models.CharField(max_length = 50)
    Prenom_P = models.CharField(max_length = 50)
    DateNaissance = models.DateField()
    Telephone_P = models.CharField(max_length = 10, help_text = 'Entrez un numero de telephone valable svp')
    Adresse_P = models.CharField(max_length = 50)

class Medecin(models.Model) : 
    Nom_M = models.CharField(max_length = 50)
    Prenom_M = models.CharField(max_length = 50)
    Telephone_M = models.CharField(max_length = 10, help_text = 'Entrez un numero de telephone valable svp')

class RendezVous(models.Model) : 
    Date_rdv = models.DateTimeField()

class Dossier (models.Model) : 
    Derniere_modif = models.DateTimeField(auto_now=True)

class Diagnostic(models.Model) : 
    Desc_diag = models.CharField(max_length = 1000)

class Ordonnance(models.Model) : 
    Designation = models.CharField(max_length = 1000)

class Medicament(models.Model) : 
    Nom_Medic = models.CharField(max_length = 50)