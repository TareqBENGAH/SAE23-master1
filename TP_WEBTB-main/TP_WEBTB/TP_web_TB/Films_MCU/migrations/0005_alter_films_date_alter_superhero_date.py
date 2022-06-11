# Generated by Django 4.0.3 on 2022-06-11 11:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Films_MCU', '0004_alter_films_date_alter_superhero_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 11, 11, 50, 44, 178815, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 11, 11, 50, 44, 146624, tzinfo=utc)),
        ),
    ]
