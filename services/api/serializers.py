from rest_framework import serializers

from services.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'commerceId',
            'employeesIds',
            'name',
            'description',
            'duration',
            'price',
            'softDelete'
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'commerceId': {'write_only': True},
            'softDelete': {'write_only': True}
        }
