from rest_framework import serializers
from .models import CarsFilms,CarsPersonages,CarsSamenvating,muziek,games

class CarsFilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsFilms
        fields = '__all__'
class CarsPersonagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsPersonages
        fields = '__all__'
class CarsSamenvatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsSamenvating
        fields = '__all__'

class muziekSerializer(serializers.ModelSerializer):
    class Meta:
        model = muziek
        fields = '__all__'

class gamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = games
        fields = '__all__'
