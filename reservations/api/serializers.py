from rest_framework import serializers

from reservations.models import ReservationState, PaymentMethod, Payment, Review, Reservation

from commerces.api.serializers import CommerceSerializer
from employees.api.serializers import EmployeeSerializer
from courts.api.serializers import CourtSerializer
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
    paymentMethod = PaymentMethodSerializer(read_only=True, source='paymentMethodId')

    class Meta:
        model = Payment
        fields = ['id', 'paymentMethod', 'paymentDate', 'receiptNumber']


class PaymentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'paymentMethodId', 'paymentDate', 'refundDate', 'receiptNumber']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'commerceId',
            'clientId',
            'reviewDate',
            'rating',
            'comment',
            'softDelete'
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'softDelete': {'write_only': True}
        }


class ReservationReadSerializer(serializers.ModelSerializer):
    commerce = CommerceSerializer(read_only=True, source='commerceId')
    client = ProfileReadSerializer(read_only=True, source='clientId')
    employee = EmployeeSerializer(read_only=True, source='employeeId')
    court = CourtSerializer(read_only=True, source='courtId')
    service = ServiceSerializer(read_only=True, source='serviceId')
    state = ReservationStateSerializer(read_only=True, source='stateId')
    payment = PaymentReadSerializer(read_only=True, source='paymentId')
    clientReview = ReviewSerializer(read_only=True, source='clientReviewId')
    commerceReview = ReviewSerializer(read_only=True, source='commerceReviewId')

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
            'clientReview',
            'commerceReview',
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
            'clientReviewId',
            'commerceReviewId',
            'reservationDate',
            'startDate',
            'endDate',
            'cancellationDate',
            'clientName',
            'clientPhone',
            'price'
        ]