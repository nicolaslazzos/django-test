from rest_framework import serializers
from commerces.models import Commerce
from provinces.api.serializers import ProvinceSerializer
from areas.api.serializers import AreaSerializer

class CommerceReadSerializer(serializers.ModelSerializer):
  commerceId = serializers.IntegerField(source='id')
  province = ProvinceSerializer(read_only=True, source='provinceId')
  area = AreaSerializer(read_only=True, source='areaId')

  class Meta:
    model = Commerce
    fields = [
      'commerceId',
      'name',
      'description',
      'area',
      'cuit',
      'email',
      'phone',
      'address',
      'city',
      'province',
      'latitude',
      'longitude',
      'profilePicture',
      'headerPicture',
      'softDelete'
    ]

class CommerceCreateUpdateSerializer(serializers.ModelSerializer):
  commerceId = serializers.IntegerField(source='id')

  class Meta:
    model = Commerce
    fields = [
      'commerceId',
      'name',
      'description',
      'areaId',
      'cuit',
      'email',
      'phone',
      'address',
      'city',
      'provinceId',
      'latitude',
      'longitude',
      'profilePicture',
      'headerPicture',
      'softDelete'
    ]