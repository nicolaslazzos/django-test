from rest_framework import serializers
from areas.models import Area

class AreaSerializer(serializers.ModelSerializer):
  areaId = serializers.CharField(source='id')

  class Meta:
    model = Area
    fields = [
      'areaId',
      'name',
      'image'
    ]

class AreaIdSerializer(serializers.ModelSerializer):
  value = serializers.CharField(source='id')
  label = serializers.CharField(source='name')
  
  class Meta:
    model = Area
    fields = [
      'value',
      'label'
    ]