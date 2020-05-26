from rest_framework import generics
from django.db.models import Q
from django.db import transaction
from django.http import JsonResponse

from schedules.models import Schedule, WorkShift, Day, ScheduleSetting
from schedules.api.serializers import WorkShiftSerializer, ScheduleSerializer, ScheduleSettingSerializer
from reservations.api.serializers import Reservation, ReservationState, Payment

import datetime

class ScheduleListAPIView(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = Schedule.objects.filter(softDelete__isnull=True)

        commerceId = self.request.query_params.get('commerceId', None)
        employeeId = self.request.query_params.get('employeeId', None)
        date = self.request.query_params.get('date', None)
        selectedDate = self.request.query_params.get('selectedDate', None)

        if self.is_param_valid(commerceId):
            qs = qs.filter(commerceId=commerceId)

        if self.is_param_valid(employeeId):
            qs = qs.filter(employeeId=employeeId)

        if self.is_param_valid(date):
            qs = qs.filter(Q(endDate__gt=date) | Q(endDate__isnull=True))

        if self.is_param_valid(selectedDate):
            qs = qs.filter(Q(startDate__lte=selectedDate), Q(endDate__isnull=True) | Q(endDate__gt=selectedDate))

        return qs.order_by('startDate')


class ScheduleCreateUpdateAPIView(generics.CreateAPIView, generics.UpdateAPIView):
    serializer_class = ScheduleSerializer
    lookup_field = 'id'

    def get_prop(self, prop, data):
        if prop in data and data[prop] is not None and data[prop] != '':
            return data[prop]
        else:
            return None

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        return Schedule.objects.filter(softDelete__isnull=True)

    def str_to_date(self, date):
        return datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

    @transaction.atomic
    def update_schedules(self, commerceId, employeeId, startDate, endDate):
        schedules = Schedule.objects.filter(Q(commerceId=commerceId), Q(endDate__isnull=True) | Q(endDate__gt=startDate))

        if self.is_param_valid(employeeId):
            schedules = schedules.filter(employeeId=employeeId)

        if self.is_param_valid(endDate):
            endDate = self.str_to_date(endDate)
            schedules = schedules.filter(startDate__lt=endDate)

        for schedule in schedules:
            if schedule.startDate < startDate and (schedule.endDate is None or startDate < schedule.endDate):
                schedule.endDate = startDate
                schedule.save()

            if schedule.startDate >= startDate and (endDate is None or (schedule.endDate and schedule.endDate <= endDate)):
                schedule.delete()

            if endDate and endDate > schedule.startDate and (schedule.endDate is None or (endDate and endDate < schedule.endDate)) and schedule.startDate >= startDate:
                schedule.startDate = endDate
                schedule.save()

    @transaction.atomic
    def cancel_reservations(self, reservations_id):
        state = ReservationState.objects.get(id='canceled')
        cancellation_date = datetime.datetime.now()

        reservations = Reservation.objects.filter(cancellationDate__isnull=True, id__in=reservations_id)

        paid_reservations = reservations.filter(paymentId__isnull=False).values_list('paymentId')
        payments = Payment.objects.filter(id__in=paid_reservations, refundDate__isnull=True).update(refundDate=cancellation_date)

        reservations.update(cancellationDate=cancellation_date, stateId=state)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            commerceId = self.get_prop('commerceId', request.data)
            employeeId = self.get_prop('employeeId', request.data)
            startDate = self.str_to_date(self.get_prop('startDate', request.data))
            endDate = self.get_prop('endDate', request.data)
            reservations_id = self.get_prop('reservationsToCancel', request.data)

            self.cancel_reservations(reservations_id)            

            self.update_schedules(commerceId, employeeId, startDate, endDate)

            schedule = serializer.save()

            return JsonResponse(data=serializer.data, status=201)

        return JsonResponse(status=400)

    @transaction.atomic
    def update(self, request, id, *args, **kwargs):
        schedule = Schedule.objects.get(id=id)
        serializer = self.serializer_class(schedule, data=request.data, partial=True)

        if serializer.is_valid():        
            endDate = self.str_to_date(self.get_prop('endDate', request.data))
            reservations_id = self.get_prop('reservationsToCancel', request.data)
            
            self.cancel_reservations(reservations_id)   

            if endDate <= schedule.startDate:
                WorkShift.objects.filter(softDelete__isnull=True, scheduleId=schedule.id).delete()
                schedule.delete()
            else:
                serializer.save()
                
            return JsonResponse(data=serializer.data, status=201)
                    
        return JsonResponse(status=400)


class WorkShiftListAPIView(generics.ListAPIView):
    serializer_class = WorkShiftSerializer

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = WorkShift.objects.filter(softDelete__isnull=True)

        scheduleId = self.request.query_params.get('scheduleId', None)

        if self.is_param_valid(scheduleId):
            qs = qs.filter(scheduleId=scheduleId)

        return qs.order_by('id')


class WorkShiftCreateUpdateAPIView(generics.CreateAPIView, generics.UpdateAPIView):
    serializer_class = WorkShiftSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return WorkShift.objects.filter(softDelete__isnull=True)


class ScheduleSettingListAPIView(generics.ListAPIView):
    serializer_class = ScheduleSettingSerializer

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = ScheduleSetting.objects.all()

        commerceId = self.request.query_params.get('commerceId', None)
        employeeId = self.request.query_params.get('employeeId', None)

        if self.is_param_valid(commerceId):
            qs = qs.filter(commerceId=commerceId)
        
        if self.is_param_valid(employeeId):
            qs = qs.filter(employeeId=employeeId)

        return qs


class ScheduleSettingCreateUpdateAPIView(generics.CreateAPIView, generics.UpdateAPIView):
    serializer_class = ScheduleSettingSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return ScheduleSetting.objects.all()
