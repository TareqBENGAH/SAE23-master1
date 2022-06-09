# Generated by Django 4.0.4 on 2022-05-19 18:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.datetime(2022, 5, 19, 18, 4, 23, 47302, tzinfo=utc))),
                ('createur', models.CharField(max_length=100)),
                ('acteurs', models.TextField()),
                ('super_pouvoir', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_film', models.CharField(max_length=100)),
                ('producteur', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.datetime(2022, 5, 19, 18, 4, 23, 238389, tzinfo=utc))),
                ('resume', models.TextField()),
                ('superhero', models.ForeignKey(null='true', on_delete=django.db.models.deletion.CASCADE, to='Films_MCU.superhero')),
            ],
        ),
    ]
