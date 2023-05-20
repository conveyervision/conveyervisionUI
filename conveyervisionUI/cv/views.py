from django.http import HttpResponse
from .models import FoodItem

def index(request):
    # Ensure the default item exists
    if not FoodItem.objects.filter(id=0).exists():
        FoodItem.objects.create(id=0, active=True, food='Salmon', location=0)

    # Fetch the default item
    item = FoodItem.objects.get(id=0)

    # Create a message displaying the item's details
    item_message = (
        f"ID: {item.id}, "
        f"Active: {item.active}, "
        f"Food: {item.food}, "
        f"Location: {item.location}, "
        f"Added: {item.added}, "
        f"Location Update: {item.location_update}"
    )

    return HttpResponse(f"Hello, world! Here's your food item: {item_message}")

