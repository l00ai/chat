# Generated by Django 3.2.5 on 2023-05-23 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20230523_0544'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
        migrations.AddField(
            model_name='translatorr',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
