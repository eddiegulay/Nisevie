# Generated by Django 4.1.1 on 2022-09-18 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankCredentials', '0006_servicerequirements'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicebenefit',
            old_name='body',
            new_name='benefit',
        ),
    ]