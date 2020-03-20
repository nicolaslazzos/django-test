from rest_framework import serializers
from provinces.models import Province

class ProvinceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Province
    fields = [
      'pk',
      'name',
      'softDelete'
    ]