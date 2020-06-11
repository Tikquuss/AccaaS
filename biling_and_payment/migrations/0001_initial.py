# Generated by Django 3.0.6 on 2020-06-03 11:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forfait',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=25, unique=True)),
                ('valeur', models.PositiveIntegerField()),
            ],
        ),
    ]