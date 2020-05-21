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

class CommerceSerializer(serializers.ModelSerializer):
    commerceId = serializers.IntegerField(read_only=True, source='id')
    province = ProvinceSerializer(read_only=True, source='provinceId')
    area = AreaSerializer(read_only=True, source='areaId')

    class Meta:
        model = Commerce
        fields = [
            'commerceId',
            'name',
            'description',
            'area',
            'areaId',
            'cuit',
            'email',
            'phone',
            'address',
            'city',
            'province',
            'provinceId',
            'latitude',
            'longitude',
            'ratingCount',
            'ratingTotal',
            'profilePicture',
            'headerPicture',
            'softDelete',
        ]
        read_only_fields = [
            'commerceId',
            'area',
            'province'
        ]
        extra_kwargs = {
            'areaId': {'write_only': True},
            'provinceId': {'write_only': True},
            'softDelete': {'write_only': True},
        }
