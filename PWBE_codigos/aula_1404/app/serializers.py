from rest_framework import serializers
from .models import Piloto, Carro

# serializers para transformar os dados das views em json e de json para views 
class PilotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        fields = '__all__'

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'