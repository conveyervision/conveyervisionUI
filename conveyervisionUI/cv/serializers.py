from rest_framework import serializers
from .models import FoodItem, CVConfig, CVSpots

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ['id', 'active', 'food']  # Example of specific fields

class CVConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = CVConfig
        fields = '__all__'  # If you want to include all fields in your API

class CVSpotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CVSpots
        fields = '__all__'  # If you want to include all fields in your API

