# Generated by Django 4.1.1 on 2022-09-18 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankCredentials', '0004_bankservice_servicebenefit'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankservice',
            name='tag_is_insurance',
            field=models.BooleanField(default=False),
        ),
    ]