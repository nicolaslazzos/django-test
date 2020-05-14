from rest_framework import serializers

from reservations.models import ReservationState, PaymentMethod, Payment, Review, Reservation

from commerces.api.serializers import CommerceReadSerializer
from employees.api.serializers import EmployeeReadSerializer
from courts.api.serializers import CourtReadSerializer
from services.api.serializers import ServiceSerializer
from profiles.api.serializers import ProfileReadSerializer


class ReservationStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationState
        fields = ['id', 'name']


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['id', 'name']


class PaymentReadSerializer(serializers.ModelSerializer):
    pymentMethod = PaymentMethodSerializer(
        read_only=True, source='paymendMethodId')

    class Meta:
        model = Payment
        fields = ['id', 'paymentMethod', 'paymentDate', 'receiptNumber']


class PaymentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'paymentMethodId', 'paymentDate', 'refundDate', 'receiptNumber']


class ReservationReadSerializer(serializers.ModelSerializer):
    commerce = CommerceReadSerializer(read_only=True, source='commerceId')
    client = ProfileReadSerializer(read_only=True, source='profileId')
    employee = EmployeeReadSerializer(read_only=True, source='employeeId')
    court = CourtReadSerializer(read_only=True, source='courtId')
    service = ServiceSerializer(read_only=True, source='serviceId')
    state = ReservationStateSerializer(read_only=True, source='stateId')
    payment = PaymentReadSerializer(read_only=True, source='paymentId')

    class Meta:
        model = Reservation
        fields = [
            'id',
            'commerce',
            'client',
            'employee',
            'court',
            'service',
            'state',
            'payment',
            'reservationDate',
            'startDate',
            'endDate',
            'cancellationDate',
            'clientName',
            'clientPhone',
            'price'
        ]


class ReservationCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            'commerceId',
            'clientId',
            'employeeId',
            'courtId',
            'serviceId',
            'stateId',
            'paymentId',
            'reservationDate',
            'startDate',
            'endDate',
            'cancellationDate',
            'clientName',
            'clientPhone',
            'price'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'reservationId',
            'commerceId',
            'clientId',
            'reviewDate',
            'rating',
            'comment'
        ]
        read_only_fields = ['id']
