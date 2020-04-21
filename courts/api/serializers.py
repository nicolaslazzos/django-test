from rest_framework import serializers

from courts.models import CourtType, GroundType, Court


class CourtTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtType
        fields = ['id', 'name', 'image']
        read_only_fields = ['id']


class GroundTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroundType
        fields = ['id', 'name']
        read_only_fields = ['id']


class CourtReadSerializer(serializers.ModelSerializer):
    courtType = CourtTypeSerializer(read_only=True, source='courtTypeId')
    groundType = GroundTypeSerializer(read_only=True, source='groundTypeId')

    class Meta:
        model = Court
        fields = [
            'id',
            'commerceId',
            'name',
            'description',
            'courtType',
            'groundType',
            'price',
            'lightPrice',
            'lightHour',
            'disabledFrom',
            'disabledTo',
            'softDelete'
        ]
        read_only_fields = ['id', 'commerceId']


class CourtCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = [
            'id',
            'commerceId',
            'name',
            'description',
            'courtTypeId',
            'groundTypeId',
            'price',
            'lightPrice',
            'lightHour',
            'disabledFrom',
            'disabledTo',
            'softDelete'
        ]
        read_only_fields = ['id']
