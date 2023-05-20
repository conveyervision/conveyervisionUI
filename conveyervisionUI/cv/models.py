from django.db import models

class FoodItem(models.Model):
    id = models.AutoField(primary_key=True)
    active = models.BooleanField(default=True)
    food = models.CharField(max_length=200)
    location = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)
    location_update = models.DateTimeField(auto_now=True)

