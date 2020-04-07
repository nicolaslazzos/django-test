from rest_framework import serializers
from profiles.models import Profile, Favorite
from provinces.api.serializers import ProvinceSerializer
from commerces.api.serializers import CommerceReadSerializer


# PROFILE SERIALIZERS

class ProfileReadSerializer(serializers.ModelSerializer):
    province = ProvinceSerializer(read_only=True, source='provinceId')
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



# FAVORITES SERIALIZERS

class FavoriteReadSerializer(serializers.ModelSerializer):
    commerce = CommerceReadSerializer(read_only=True, source='commerceId')

    class Meta:
        model = Favorite
        fields = ['commerce']

class FavoriteCommerceIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['commerceId']
