# Generated by Django 4.0.6 on 2022-09-17 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0007_rename_is_current_savingplan_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='savingplan',
            name='is_fixed',
            field=models.BooleanField(default=False),
        ),
    ]