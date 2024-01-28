# Generated by Django 5.0.1 on 2024-01-27 13:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0004_medecin_specialite_alter_rendezvous_num_patient"),
    ]

    operations = [
        migrations.AddField(
            model_name="rendezvous",
            name="departement",
            field=models.CharField(
                choices=[
                    ("Card", "Cardiology"),
                    ("Neuro", "Neurology"),
                    ("Urol", "Urology"),
                    ("Rheum", "Rheumatology"),
                    ("ENT", "Ear, Nose, and Throat"),
                ],
                default=1,
                max_length=50,
            ),
            preserve_default=False,
        ),
    ]