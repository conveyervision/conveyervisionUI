# Generated by Django 4.2.1 on 2023-05-31 00:50

from django.db import migrations
from django.core.management import call_command

fixture = '0004_ConfigSeed'

def load_fixture(apps, schema_editor):
    call_command('loaddata', fixture)

class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_CVSpotsCVConfig'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]

