from rest_framework import Serializer
from .models import Car

class CarSerializer(Serializer.ModelSerializer):
    class Meta:
        model = Car
        fields =['id' ,'make', 'model', 'year', 'price']