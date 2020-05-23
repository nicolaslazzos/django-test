from rest_framework import serializers

from employees.models import Employee, Role
from profiles.api.serializers import ProfileReadSerializer


class RoleIdSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id')
    label = serializers.CharField(source='name')

    class Meta:
        model = Role
        fields = ['value', 'label']


class RoleSerializer(serializers.ModelSerializer):
    roleId = serializers.CharField(source='id')

    class Meta:
        model = Role
        fields = ['roleId', 'name', 'value']
        read_only_fields = ['roleId']


class EmployeeSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True, source='roleId')
    profile = ProfileReadSerializer(read_only=True, source='profileId')
    profile_fields = ['firstName', 'lastName', 'email', 'phone', 'profilePicture']

    class Meta:
        model = Employee
        fields = [
            'id',
            'commerceId',
            'profileId',
            'profile',
            'role',
            'roleId',
            'inviteDate',
            'startDate',
            'softDelete'
        ]
        read_only_fields = ['id', 'firstName', 'lastName', 'email', 'phone', 'profilePicture']
        extra_kwargs = {
            'softDelete': { 'write_only': True },
        }

    def to_representation(self, instance):
        data = super(EmployeeSerializer, self).to_representation(instance)
        profile = data.pop('profile')

        for key, val in profile.items():
            if key in self.profile_fields:
                data.update({key: val})

        return data
