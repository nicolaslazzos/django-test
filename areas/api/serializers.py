from rest_framework import serializers
from areas.models import Area

class AreaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Area
    fields = [
      'areaId',
      'name'
    ]

class AreaIdSerializer(serializers.ModelSerializer):
  value = serializers.CharField(source='areaId')
  label = serializers.CharField(source='name')
  
  class Meta:
    model = Area
    fields = [
      'value',
      'label'
    ]