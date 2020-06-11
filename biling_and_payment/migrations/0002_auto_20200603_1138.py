# Generated by Django 3.0.6 on 2020-06-03 11:38

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('biling_and_payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompteUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('solde', models.DecimalField(decimal_places=2, max_digits=6)),
                ('actif', models.BooleanField(default=True)),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('date_expiration', models.DateTimeField(default=datetime.datetime(2020, 6, 4, 11, 38, 19, 853707))),
            ],
        ),
        migrations.AlterField(
            model_name='forfait',
            name='valeur',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]