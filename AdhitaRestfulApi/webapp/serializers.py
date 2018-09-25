from rest_framework import serializers
from .models import car
from .models import computer

class carsSerializer(serializers.ModelSerializer):

    class Meta:
        model = car
        fields = ('name', 'model_name', 'color')

class computerSerializer(serializers.ModelSerializer):

    class Meta:
        model = computer
        fields = '__all__'