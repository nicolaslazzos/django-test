from rest_framework import serializers
from profiles.models import Profile, Favorite
from provinces.api.serializers import ProvinceSerializer
from commerces.api.serializers import CommerceReadSerializer


# PROFILE SERIALIZERS

class ProfileReadSerializer(serializers.ModelSerializer):
    province = ProvinceSerializer(read_only=True, source='provinceId')
    clientId = serializers.CharField(source='id') # provisorio
    profileId = serializers.CharField(source='id')

    class Meta:
        model = Profile
        fields = [
            'clientId',
            'profileId',
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

class FavoriteIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'profileId', 'commerceId']
        read_only_fields = ['id']
