from rest_framework import serializers

from employees.models import Employee, Role
from profiles.api.serializers import ProfileReadSerializer


class RoleSerializer(serializers.ModelSerializer):
    roleId = serializers.CharField(source='id')

    class Meta:
        model = Role
        fields = ['roleId', 'name', 'value']
        read_only_fields = ['roleId']


class EmployeeReadSerializer(serializers.ModelSerializer):
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
            'inviteDate',
            'startDate'
        ]

    def to_representation(self, instance):
        data = super(EmployeeReadSerializer, self).to_representation(instance)
        profile = data.pop('profile')

        for key, val in profile.items():
            if key in self.profile_fields:
                data.update({key: val})

        return data


class EmployeeCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'profileId',
            'commerceId',
            'roleId',
            'inviteDate',
            'startDate',
            'softDelete'
        ]
