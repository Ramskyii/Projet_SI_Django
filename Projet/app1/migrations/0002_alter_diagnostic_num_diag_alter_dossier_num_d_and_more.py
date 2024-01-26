# Generated by Django 5.0.1 on 2024-01-26 14:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="diagnostic",
            name="Num_Diag",
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="dossier",
            name="Num_D",
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="medecin",
            name="Num_M",
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="medicament",
            name="Code_Medic",
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="ordonnance",
            name="Num_ord",
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="patient",
            name="Num_P",
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="rendezvous",
            name="Num_rdv",
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
