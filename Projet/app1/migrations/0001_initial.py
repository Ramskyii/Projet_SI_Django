# Generated by Django 5.0.1 on 2024-01-26 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Diagnostic",
            fields=[
                ("Num_Diag", models.AutoField(primary_key=True, serialize=False)),
                ("Desc_diag", models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="Dossier",
            fields=[
                ("Num_D", models.AutoField(primary_key=True, serialize=False)),
                ("Derniere_modif", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Medicament",
            fields=[
                ("Code_Medic", models.AutoField(primary_key=True, serialize=False)),
                ("Nom_Medic", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Ordonnance",
            fields=[
                ("Num_ord", models.AutoField(primary_key=True, serialize=False)),
                ("Designation", models.CharField(max_length=1000)),
                ("Medicaments", models.ManyToManyField(to="app1.medicament")),
                (
                    "Num_diagnostic",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.diagnostic",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="diagnostic",
            name="Num_ordonnance",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="app1.ordonnance"
            ),
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                ("Num_P", models.AutoField(primary_key=True, serialize=False)),
                ("Nom_P", models.CharField(max_length=50)),
                ("Prenom_P", models.CharField(max_length=50)),
                ("DateNaissance", models.DateField()),
                (
                    "Telephone_P",
                    models.CharField(
                        help_text="Entrez un numero de telephone valable svp",
                        max_length=10,
                    ),
                ),
                ("Adresse_P", models.CharField(max_length=50)),
                (
                    "num_dossier",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="app1.dossier"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="dossier",
            name="Num_Patient",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="app1.patient"
            ),
        ),
        migrations.CreateModel(
            name="RendezVous",
            fields=[
                ("Num_rdv", models.AutoField(primary_key=True, serialize=False)),
                ("Date_rdv", models.DateTimeField()),
                (
                    "Num_Diagnostic",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.diagnostic",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="patient",
            name="Num_rendezvous",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app1.rendezvous"
            ),
        ),
        migrations.CreateModel(
            name="Medecin",
            fields=[
                ("Num_M", models.AutoField(primary_key=True, serialize=False)),
                ("Nom_M", models.CharField(max_length=50)),
                ("Prenom_M", models.CharField(max_length=50)),
                (
                    "Telephone_M",
                    models.CharField(
                        help_text="Entrez un numero de telephone valable svp",
                        max_length=10,
                    ),
                ),
                (
                    "Num_rendezvous",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.rendezvous",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="diagnostic",
            name="Num_rendezvous",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="app1.rendezvous"
            ),
        ),
    ]
