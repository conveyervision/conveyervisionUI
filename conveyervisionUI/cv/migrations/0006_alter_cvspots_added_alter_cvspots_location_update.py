# Generated by Django 4.2.1 on 2023-06-22 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_alter_cvspots_added_alter_cvspots_location_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvspots',
            name='added',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='cvspots',
            name='location_update',
            field=models.DateTimeField(null=True),
        ),
    ]
