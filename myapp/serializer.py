from rest_framework import serializers
from .models import Files, Weather


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ['file']
        depth = 1
        
class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'