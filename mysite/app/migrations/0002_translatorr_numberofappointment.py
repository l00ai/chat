# Generated by Django 3.2.5 on 2023-05-18 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='translatorr',
            name='numberOfAppointment',
            field=models.IntegerField(default=0),
        ),
    ]
