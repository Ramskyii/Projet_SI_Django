from django.db import models

class Patient(models.Model) : 
    Num_P = models.AutoField(primary_key=True, default=1)
    Nom_P = models.CharField(max_length = 50)
    Prenom_P = models.CharField(max_length = 50)
    DateNaissance = models.DateField()
    Telephone_P = models.CharField(max_length = 10, help_text = 'Entrez un numero de telephone valable svp')
    Adresse_P = models.CharField(max_length = 50)
    
    

class Medecin(models.Model) : 
    Num_M = models.AutoField(primary_key=True, default=1)
    Nom_M = models.CharField(max_length = 50)
    Prenom_M = models.CharField(max_length = 50)
    Telephone_M = models.CharField(max_length = 10, help_text = 'Entrez un numero de telephone valable svp')
    

class RendezVous(models.Model) : 
    Num_rdv = models.AutoField(primary_key=True, default=1)
    Date_rdv = models.DateTimeField()
    salle = models.ForeignKey('Salle', on_delete=models.CASCADE)
    Num_Patient = models.OneToOneField(Patient,on_delete = models.CASCADE)
    Num_Medecin = models.ForeignKey(Medecin,on_delete = models.CASCADE)
    

class Dossier(models.Model) : 
    Num_D = models.AutoField(primary_key=True, default=1)
    Derniere_modif = models.DateTimeField(auto_now=True)
    Num_Patient = models.OneToOneField(Patient,on_delete = models.CASCADE)

class Diagnostic(models.Model) : 
    Num_Diag = models.AutoField(primary_key=True, default=1)
    Desc_diag = models.CharField(max_length = 1000)
    Num_rendezvous = models.OneToOneField(RendezVous,on_delete = models.CASCADE)
    

class Ordonnance(models.Model) : 
    Num_ord = models.AutoField(primary_key=True, default= 1)
    Designation = models.CharField(max_length = 1000)
    Num_diagnostic = models.OneToOneField(Diagnostic,on_delete = models.CASCADE)
    Medicaments = models.ManyToManyField('Medicament')
    

class Medicament(models.Model) : 
    Code_Medic = models.AutoField(primary_key=True, default=1)
    Nom_Medic = models.CharField(max_length = 50)

class Salle (models.Model) : 
    Num_salle = models.AutoField(primary_key=True, default=1)
    choix_de_type = [
        ('operation', 'salle d\'opération'),
        ('consultation', 'salle de consultation'),
    ]
    type_salle = models.CharField(max_length = 20, choices = choix_de_type)