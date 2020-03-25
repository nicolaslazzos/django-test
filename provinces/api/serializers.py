from rest_framework import serializers
from provinces.models import Province

class ProvinceSerializer(serializers.ModelSerializer):
  provinceId = serializers.IntegerField(source='pk')

  class Meta:
    model = Province
    fields = [
      'provinceId',
      'name'
    ]

class ProvinceIdSerializer(serializers.ModelSerializer):
  value = serializers.IntegerField(source='pk')
  label = serializers.CharField(source='name')
  
  class Meta:
    model = Province
    fields = [
      'value',
      'label'
    ]

class ProvinceNameSerializer(serializers.ModelSerializer):
  value = serializers.CharField(source='name')
  label = serializers.CharField(source='name')
  
  class Meta:
    model = Province
    fields = [
      'value',
      'label'
    ]