from rest_framework import generics
from django.db import transaction
from django.http import JsonResponse

from courts.models import CourtType, GroundType, Court
from reservations.models import Reservation, ReservationState, Payment

from courts.api.serializers import CourtTypeSerializer, CourtTypeIdSerializer, GroundTypeIdSerializer, GroundTypeSerializer, CourtSerializer, CourtSerializer

import datetime

class CourtListAPIView(generics.ListAPIView):
    serializer_class = CourtSerializer
    lookup_url_kwarg = 'id'

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = Court.objects.filter(softDelete__isnull=True).order_by('name')

        commerceId = self.request.query_params.get('commerceId', None)
        courtTypeId = self.request.query_params.get('courtTypeId', None)

        if self.is_param_valid(commerceId):
            qs = qs.filter(commerceId=commerceId)

        if self.is_param_valid(courtTypeId):
            qs = qs.filter(courtTypeId=courtTypeId)

        return qs


class CourtCreateRetrieveUpdateDestroyAPIView(generics.CreateAPIView, generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = CourtSerializer

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        return Court.objects.filter(softDelete__isnull=True)

    def court_name_exists(self, id, name, commerceId):
        qs = Court.objects.filter(name=name, commerceId=commerceId)

        if id is not None:
            qs = qs.exclude(id=id)

        return qs.count() >= 1

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        commerceId = request.data['commerceId']
        name = request.data['name']

        if self.court_name_exists(None, name, commerceId):
            return JsonResponse(data={ 'on_court_exists': True })

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(data=serializer.data, status=201)

        return JsonResponse(status=400)

    @transaction.atomic
    def update(self, request, id, *args, **kwargs):
        court = Court.objects.get(id=id)
        serializer = self.serializer_class(court, data=request.data, partial=True)

        name = request.data['name']
        commerceId = court.commerceId.id

        if self.court_name_exists(id, name, commerceId):
            return JsonResponse(data={ 'on_court_exists': True })

        if serializer.is_valid():
            if 'reservationsToCancel' in request.data and len(request.data['reservationsToCancel']):
                state = ReservationState.objects.get(id='canceled')
                cancellation_date = datetime.datetime.now()

                reservations = Reservation.objects.filter(cancellationDate__isnull=True, id__in=request.data['reservationsToCancel'], courtId=id)

                paid_reservations = reservations.filter(paymentId__isnull=False).values_list('paymentId')
                payments = Payment.objects.filter(id__in=paid_reservations, refundDate__isnull=True).update(refundDate=cancellation_date)

                reservations.update(cancellationDate=cancellation_date, stateId=state)

            serializer.save()

            return JsonResponse(data=serializer.data, status=201)

        return JsonResponse(status=400)

    @transaction.atomic
    def delete(self, request, id):
        court = Court.objects.get(id=id)
        delete_date = datetime.datetime.now()
        serializer = self.serializer_class(court, data={ 'softDelete': delete_date }, partial=True)

        if serializer.is_valid():
            reservations_id = self.request.query_params.get('reservationsToCancel', None)

            if self.is_param_valid(reservations_id):
                reservations_id = map(lambda id: int(id), reservations_id.split(','))
                state = ReservationState.objects.get(id='canceled')

                reservations = Reservation.objects.filter(cancellationDate__isnull=True, id__in=reservations_id, courtId=id)

                paid_reservations = reservations.filter(paymentId__isnull=False).values_list('paymentId')
                payments = Payment.objects.filter(id__in=paid_reservations, refundDate__isnull=True).update(refundDate=delete_date)

                reservations.update(cancellationDate=delete_date, stateId=state)

            serializer.save()

            return JsonResponse(data=serializer.data, status=201)

        return JsonResponse(data='wrong parameters', status=400, safe=False)


class CourtTypeListAPIView(generics.ListAPIView):
    serializer_class = CourtTypeSerializer

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = CourtType.objects.filter(softDelete__isnull=True).order_by('name')
        
        commerceId = self.request.query_params.get('commerceId', None)

        if self.is_param_valid(commerceId):
            commerce_courts = Court.objects.filter(softDelete__isnull=True, commerceId=commerceId).values_list('courtTypeId')
            qs = qs.filter(id__in=commerce_courts)

        return qs

class CourtTypeIdListAPIView(generics.ListAPIView):
    serializer_class = CourtTypeIdSerializer

    def get_queryset(self):
        return CourtType.objects.filter(softDelete__isnull=True).order_by('name')

class GroundTypeListAPIView(generics.ListAPIView):
    serializer_class = GroundTypeSerializer

    def get_queryset(self):
        return GroundType.objects.filter(softDelete__isnull=True).order_by('name')

class GroundTypeIdListAPIView(generics.ListAPIView):
    serializer_class = GroundTypeIdSerializer

    def get_queryset(self):
        return GroundType.objects.filter(softDelete__isnull=True).order_by('name')
