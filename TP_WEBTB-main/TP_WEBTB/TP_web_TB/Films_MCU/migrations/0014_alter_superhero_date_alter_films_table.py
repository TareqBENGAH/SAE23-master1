# Generated by Django 4.0.3 on 2022-06-11 15:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Films_MCU', '0013_acteurs_authgroup_authgrouppermissions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 11, 15, 40, 18, 103464, tzinfo=utc)),
        ),
        migrations.AlterModelTable(
            name='films',
            table='Films',
        ),
    ]
