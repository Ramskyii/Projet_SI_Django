# Generated by Django 5.0.1 on 2024-01-27 16:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0006_alter_salle_type_salle"),
    ]

    operations = [
        migrations.AlterField(
            model_name="salle",
            name="type_salle",
            field=models.CharField(
                choices=[
                    ("consultation", "salle de consultation"),
                    ("operation", "salle d'opération"),
                ],
                max_length=50,
            ),
        ),
    ]
