from rest_framework import serializers

from notifications.models import NotificationToken, NotificationType, Notification
from reservations.api.serializers import ReservationReadSerializer


class NotificationTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationToken
        fields = ['id', 'profileId', 'softDelete']
        extra_kwargs = {
            'profileId': {'write_only': True},
            'softDelete': {'write_only': True}
        }


class NotificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationType
        fields = ['id', 'name', 'softDelete']
        read_only_fields = ['id']
        extra_kwargs = {
            'softDelete': {'write_only': True},
        }


class NotificationSerializer(serializers.ModelSerializer):
    reservation = ReservationReadSerializer(read_only=True, source='reservationId')
    notificationType = NotificationTypeSerializer(read_only=True, source='notificationTypeId')

    class Meta:
        model = Notification
        fields = [
            'id',
            'commerceId',
            'profileId',
            'employeeId',
            'reservation',
            'reservationId',
            'notificationType',
            'notificationTypeId',
            'title',
            'body',
            'read',
            'date',
            'acceptanceDate',
            'rejectionDate',
            'softDelete',
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'reservationId': {'write_only': True},
            'softDelete': {'write_only': True},
            'notificationTypeId': {'write_only': True},
        }
