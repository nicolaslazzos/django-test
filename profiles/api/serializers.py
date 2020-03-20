from rest_framework import serializers
from profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'pk',
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
        # read_only_fields = ['pk', 'clientId', 'email']
