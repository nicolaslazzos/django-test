from rest_framework import generics

from reservations.api.serializers import PaymentReadSerializer, PaymentCreateUpdateSerializer, ReservationReadSerializer, ReservationCreateUpdateSerializer, ReviewSerializer
from reservations.models import ReservationState, PaymentMethod, Payment, Reservation, Review
from courts.models import Court


class PaymentCreateUpdateAPIView(generics.UpdateAPIView, generics.CreateAPIView):
    serializer_class = PaymentCreateUpdateSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Payment.objects.filter(refundDate__isnull=True)


class ReservationListAPIView(generics.ListAPIView):
    serializer_class = ReservationReadSerializer

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = Reservation.objects.filter(cancellationDate__isnull=True)

        commerceId = self.request.query_params.get('commerceId', None)
        employeeId = self.request.query_params.get('employeeId', None)
        clientId = self.request.query_params.get('clientId', None)
        courtId = self.request.query_params.get('courtId', None)
        courtTypeId = self.request.query_params.get('courtTypeId', None)
        startDate = self.request.query_params.get('startDate', None)
        endDate = self.request.query_params.get('endDate', None)

        if self.is_param_valid(commerceId):
            qs = qs.filter(commerceId=commerceId)

        if self.is_param_valid(employeeId):
            qs = qs.filter(employeeId=employeeId)

        if self.is_param_valid(clientId):
            qs = qs.filter(clientId=clientId)

        if self.is_param_valid(courtId):
            qs = qs.filter(courtId=courtId)

        if self.is_param_valid(courtTypeId):
            qs = qs.filter(courtId__courtTypeId=courtTypeId)

        if self.is_param_valid(startDate):
            qs = qs.filter(endDate__gt=startDate)

        if self.is_param_valid(endDate):
            qs = qs.filter(startDate__lt=endDate)

        return qs.order_by('-startDate')


class ReservationRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ReservationReadSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Reservation.objects.filter(cancellationDate__isnull=True)


class ReservationCreateUpdateAPIView(generics.CreateAPIView, generics.UpdateAPIView):
    serializer_class = ReservationCreateUpdateSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Reservation.objects.filter(cancellationDate__isnull=True)


class ReviewListAPIView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = Review.objects.filter(softDelete__isnull=True)

        clientId = self.request.query_params.get('clientId', None)
        commerceId = self.request.query_params.get('commerceId', None)

        if self.is_param_valid(commerceId):
            qs = qs.filter(commerceId=commerceId)

        if self.is_param_valid(clientId):
            qs = qs.filter(clientId=clientId)

        return qs.order_by('-reviewDate')


class ReviewRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ReviewSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Review.objects.filter(softDelete__isnull=True)


class ReviewCreateUpdateAPIView(generics.CreateAPIView, generics.UpdateAPIView):
    serializer_class = ReviewSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Review.objects.filter(softDelete__isnull=True)
