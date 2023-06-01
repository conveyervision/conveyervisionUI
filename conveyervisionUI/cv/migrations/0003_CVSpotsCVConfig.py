# Generated by Django 4.2.1 on 2023-06-01 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_load_yum_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CVConfig',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('completed', models.BooleanField(default=False)),
                ('num_spots', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CVSpots',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('food', models.CharField(max_length=200)),
                ('location', models.IntegerField()),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('location_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'CVSpots',
            },
        ),
    ]