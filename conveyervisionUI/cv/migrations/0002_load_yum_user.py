# Generated by Django 4.2.1 on 2023-05-30 15:23

from django.db import migrations
from django.core.management import call_command

fixture = '0002_UserSeed'

def load_fixture(apps, schema_editor):
    call_command('loaddata', fixture)

class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]
