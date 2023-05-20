from django.shortcuts import render
from .models import FoodItem

def index(request):
    # Ensure the default item exists
    if not FoodItem.objects.filter(id=0).exists():
        FoodItem.objects.create(id=0, active=True, food='Salmon', location=0)

    # Fetch the default item
    item = FoodItem.objects.get(id=0)

    # Pass the food item to the template
    return render(request, 'cv/index.html', {'fooditem': item})

