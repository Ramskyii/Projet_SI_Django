# Generated by Django 5.0.1 on 2024-01-26 19:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="diagnostic",
            name="Num_ordonnance",
        ),
        migrations.RemoveField(
            model_name="medecin",
            name="Num_rendezvous",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="Num_rendezvous",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="num_dossier",
        ),
        migrations.RemoveField(
            model_name="rendezvous",
            name="Num_Diagnostic",
        ),
    ]
