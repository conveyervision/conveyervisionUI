from django.core.management.base import BaseCommand
from cv.models import FoodItem

class Command(BaseCommand):
    help = 'Seeds the database with a default FoodItem'

    def handle(self, *args, **options):
        if not FoodItem.objects.filter(id=0).exists():
            FoodItem.objects.create(id=0, active=True, food='Salmon', location=0)

