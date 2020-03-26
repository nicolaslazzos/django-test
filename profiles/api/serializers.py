from rest_framework import serializers
from profiles.models import Profile
from provinces.api.serializers import ProvinceSerializer


class ProfileReadSerializer(serializers.ModelSerializer):
    province = ProvinceSerializer(read_only=False, source='provinceId')
    clientId = serializers.CharField(source='id')

    class Meta:
        model = Profile
        fields = [
            'clientId',
            'firstName',
            'lastName',
            'email',
            'phone',
            'profilePicture',
            'province',
            'commerceId',
            'softDelete'
        ]


class ProfileCreateUpdateSerializer(serializers.ModelSerializer):
    clientId = serializers.CharField(source='id')

    class Meta:
        model = Profile
        fields = [
            'clientId',
            'firstName',
            'lastName',
            'email',
            'phone',
            'profilePicture',
            'provinceId',
            'commerceId',
            'softDelete'
        ]
