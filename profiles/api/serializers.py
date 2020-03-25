from rest_framework import serializers
from profiles.models import Profile
from provinces.api.serializers import ProvinceSerializer
from provinces.models import Province


class ProfileSerializer(serializers.ModelSerializer):
    province = ProvinceSerializer(read_only=True, source='provinceId')

    class Meta:
        model = Profile
        fields = [
            'id',
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
