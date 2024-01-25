from django.db import models

class Patient(models.Model) : 
    Num_P = models.AutoField(primary_key=True)
    Nom_P = models.CharField(max_length = 50)
    Prenom_P = models.CharField(max_length = 50)
    DateNaissance = models.DateField()
    Telephone_P = models.CharField(max_length = 10, help_text = 'Entrez un numero de telephone valable svp')
    Adresse_P = models.CharField(max_length = 50)
    Num_dossier = models.ForeignKey('Dossier', on_delete = models.CASCADE )


class Medecin(models.Model) : 
    Num_M = models.AutoField(primary_key=True)
    Nom_M = models.CharField(max_length = 50)
    Prenom_M = models.CharField(max_length = 50)
    Telephone_M = models.CharField(max_length = 10, help_text = 'Entrez un numero de telephone valable svp')

class RendezVous(models.Model) : 
    Num_rdv = models.AutoField(primary_key=True)
    Date_rdv = models.DateTimeField()
    Num_patient = models.ForeignKey(Patient, on_delete = models.CASCADE) 
    Num_medecin = models.ForeignKey(Medecin, on_delete = models.CASCADE)

class Dossier(models.Model) : 
    Num_D = models.AutoField(primary_key=True)
    Derniere_modif = models.DateTimeField(auto_now=True)

class Diagnostic(models.Model) : 
    Num_Diag = models.AutoField(primary_key=True)
    Desc_diag = models.CharField(max_length = 1000)
    Num_rdv = models.ForeignKey(RendezVous, on_delete = models.CASCADE)

class Ordonnance(models.Model) : 
    Num_odr = models.AutoField(primary_key=True)
    Designation = models.CharField(max_length = 1000)
    Num_diagnostic = models.ForeignKey(Diagnostic, on_delete = models.CASCADE)

class Medicament(models.Model) : 
    Code_Medic = models.AutoField(primary_key=True)
    Nom_Medic = models.CharField(max_length = 50)
    Num_ordonnance = models.ForeignKey(Ordonnance, on_delete = models.CASCADE)