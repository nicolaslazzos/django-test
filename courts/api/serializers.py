from rest_framework import serializers

from courts.models import CourtType, GroundType, Court


class CourtTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtType
        fields = ['id', 'name', 'image']
        read_only_fields = ['id']


class CourtTypeIdSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source='id')
    label = serializers.CharField(source='name')

    class Meta:
        model = CourtType
        fields = ['value', 'label']


class GroundTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroundType
        fields = ['id', 'name']
        read_only_fields = ['id']


class GroundTypeIdSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source='id')
    label = serializers.CharField(source='name')

    class Meta:
        model = GroundType
        fields = ['value', 'label']


class CourtSerializer(serializers.ModelSerializer):
    courtType = CourtTypeSerializer(read_only=True, source='courtTypeId')
    groundType = GroundTypeSerializer(read_only=True, source='groundTypeId')

    class Meta:
        model = Court
        fields = [
            'id',
            'commerceId',
            'name',
            'description',
            'courtTypeId', # write only maybe
            'courtType',
            'groundTypeId', # write only maybe
            'groundType',
            'price',
            'lightPrice',
            'lightHour',
            'disabledFrom',
            'disabledTo',
            'softDelete'
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'softDelete': { 'write_only': True },
            'commerceId': { 'write_only': True },
        }
