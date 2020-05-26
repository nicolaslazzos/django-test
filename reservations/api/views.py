from rest_framework import generics
from django.db import transaction
from django.db.models import Q
from django.http import JsonResponse

from reservations.api.serializers import PaymentReadSerializer, PaymentCreateUpdateSerializer, ReservationReadSerializer, ReservationCreateUpdateSerializer, ReviewSerializer
from reservations.models import ReservationState, PaymentMethod, Payment, Reservation, Review
from courts.models import Court
from profiles.models import Profile
from commerces.models import Commerce

import datetime


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

    def get_prop(self, prop, data):
        if prop in data and data[prop] is not None and data[prop] != '':
            return data[prop]
        else:
            return None

    def get_queryset(self):
        return Reservation.objects.filter(cancellationDate__isnull=True)

    def reservation_exists(self, commerceId, employeeId, courtId, startDate, endDate):
        qs = self.get_queryset().filter(commerceId=commerceId, startDate__lt=endDate, endDate__gt=startDate)

        if employeeId is not None:
            qs = qs.filter(employeeId=employeeId)

        if courtId is not None:
            qs = qs.filter(courtId=courtId)

        return qs.count() >= 1

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            commerceId = self.get_prop('commerceId', request.data)
            employeeId = self.get_prop('employeeId', request.data)
            courtId = self.get_prop('courtId', request.data)
            startDate = self.get_prop('startDate', request.data)
            endDate = self.get_prop('endDate', request.data)

            if self.reservation_exists(commerceId, employeeId, courtId, startDate, endDate):
                return JsonResponse(data={ 'on_reservation_exists': True })

            serializer.save()

            return JsonResponse(data=serializer.data, status=201)

        return JsonResponse(status=400)


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


class ReviewCreateRetrieveUpdateDestroyAPIView(generics.CreateAPIView, generics.UpdateAPIView, generics.RetrieveAPIView, generics.DestroyAPIView):
    serializer_class = ReviewSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Review.objects.filter(softDelete__isnull=True)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            review = serializer.save()
            
            reservationId = request.data['reservationId']
            rating = request.data['rating']

            reservation = Reservation.objects.get(id=reservationId)

            if 'clientId' in request.data:
                reservation.commerceReviewId = review
                receiver = Profile.objects.get(id=request.data['clientId'])
            else:
                reservation.clientReviewId = review
                receiver = Commerce.objects.get(id=request.data['commerceId'])

            reservation.save()

            receiver.ratingCount = receiver.ratingCount + 1
            receiver.ratingTotal = receiver.ratingTotal + rating
            receiver.save()

            return JsonResponse(data=serializer.data, status=201)

        return JsonResponse(status=400)

    @transaction.atomic
    def update(self, request, id, *args, **kwargs):
        review = Review.objects.get(id=id)
        serializer = self.serializer_class(review, data=request.data, partial=True)

        if serializer.is_valid():
            profile = review.clientId
            commerce = review.commerceId
            rating = request.data['rating']

            if profile is not None:
                receiver = profile
            else:
                receiver = commerce

            receiver.ratingTotal = receiver.ratingTotal - review.rating + rating
            receiver.save()

            serializer.save()

            return JsonResponse(data=serializer.data, status=201)

        return JsonResponse(status=400)

    @transaction.atomic
    def delete(self, request, id):
        review = Review.objects.get(id=id)
        delete_date = datetime.datetime.now()
        serializer = self.serializer_class(review, data={ 'softDelete': delete_date }, partial=True)

        if serializer.is_valid():
            profile = review.clientId
            commerce = review.commerceId

            if profile is not None:
                reservation = Reservation.objects.get(commerceReviewId=id)
                reservation.commerceReviewId = None
                receiver = profile
            else:
                reservation = Reservation.objects.get(clientReviewId=id)
                reservation.clientReviewId = None
                receiver = commerce

            reservation.save()

            receiver.ratingCount = receiver.ratingCount - 1
            receiver.ratingTotal = receiver.ratingTotal - review.rating
            receiver.save()

            serializer.save()

            return JsonResponse(data=serializer.data, status=201)

        return JsonResponse(status=400)
