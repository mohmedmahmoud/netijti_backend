from rest_framework import serializers
from .models import Sector, Result

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = [ 'name', 'description', 'created_at']

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = [ 'number', 'name', 'score','metadata', 'created_at']
