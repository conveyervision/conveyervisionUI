from django.contrib import admin
from cv.models import FoodItem, CVConfig, CVSpots

# Register your models here.
admin.site.register(FoodItem)
admin.site.register(CVConfig)
admin.site.register(CVSpots)
