from rest_framework import serializers

from commerces.models import Commerce, Area

from provinces.api.serializers import ProvinceSerializer

# AREAS

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


# COMMERCES

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
    ]

class CommerceCreateUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Commerce
    fields = [
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