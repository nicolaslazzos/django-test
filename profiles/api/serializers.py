from rest_framework import serializers
from profiles.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = [
      'pk',
      'profileId',
      'firstName',
      'lastName',
      'email',
      'phone',
      'provinceId',
      'softDelete'
    ]
    # read_only_fields = ['pk', 'profileId', 'email']