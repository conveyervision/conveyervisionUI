from django.shortcuts import render
from .models import FoodItem

def home(request):
    item = FoodItem.objects.first()  # gets the first FoodItem
    context = {
        'fooditem': item,
    }
    return render(request, 'cv/home.html', context)

