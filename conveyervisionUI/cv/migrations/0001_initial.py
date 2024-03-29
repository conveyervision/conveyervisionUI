# Generated by Django 4.2.1 on 2023-05-20 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('food', models.CharField(max_length=200)),
                ('location', models.IntegerField()),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('location_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
