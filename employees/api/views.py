from rest_framework import generics
from django.db import transaction
from django.http import JsonResponse

from employees.models import Role, Employee
from schedules.models import Schedule, WorkShift
from reservations.models import Reservation, ReservationState, Payment
from employees.api.serializers import RoleSerializer, RoleIdSerializer, EmployeeSerializer, EmployeeSerializer

import datetime


class RoleListAPIView(generics.ListAPIView):
    serializer_class = RoleSerializer

    def get_queryset(self):
        return Role.objects.filter(softDelete__isnull=True).order_by('name')


class RoleIdListAPIView(generics.ListAPIView):
    serializer_class = RoleIdSerializer

    def get_queryset(self):
        return Role.objects.filter(softDelete__isnull=True).order_by('name')


class EmployeeListAPIView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = Employee.objects.filter(softDelete__isnull=True)

        commerceId = self.request.query_params.get('commerceId', None)
        profileId = self.request.query_params.get('profileId', None)
        startDate = self.request.query_params.get('startDate', None)
        visible = self.request.query_params.get('visible', None)
        employeesIds = self.request.query_params.get('employeesIds', None)

        if self.is_param_valid(commerceId):
            qs = qs.filter(commerceId=commerceId)

        if self.is_param_valid(profileId):
            qs = qs.filter(profileId=profileId)

        if self.is_param_valid(startDate):
            qs = qs.filter(startDate__isnull=False)

        if self.is_param_valid(visible):
            qs = qs.filter(visible=True)

        if self.is_param_valid(employeesIds):
            employeesIds = map(lambda id: int(id), employeesIds.split(','))
            qs = qs.filter(id__in=employeesIds)

        return qs.order_by('profileId__firstName', 'profileId__lastName')


class EmployeeCreateRetrieveUpdateDestroyAPIView(generics.CreateAPIView, generics.UpdateAPIView, generics.RetrieveAPIView, generics.DestroyAPIView):
    serializer_class = EmployeeSerializer
    lookup_field = 'id'

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        return Employee.objects.filter(softDelete__isnull=True)

    @transaction.atomic
    def delete(self, request, id):
        employee = Employee.objects.get(id=id)
        delete_date = datetime.datetime.now()
        serializer = self.serializer_class(employee, data={ 'softDelete': delete_date }, partial=True)

        if serializer.is_valid():
            # delete employee schedules
            schedules = Schedule.objects.filter(softDelete__isnull=True, employeeId=id)
            WorkShift.objects.filter(softDelete__isnull=True, scheduleId__in=schedules).update(softDelete=delete_date)
            schedules.update(softDelete=delete_date)

            # cancel employee reservations
            reservations_id = self.request.query_params.get('reservationsToCancel', None)

            if self.is_param_valid(reservations_id):
                reservations_id = map(lambda id: int(id), reservations_id.split(','))
                state = ReservationState.objects.get(id='canceled')

                reservations = Reservation.objects.filter(cancellationDate__isnull=True, id__in=reservations_id, employeeId=id)

                paid_reservations = reservations.filter(paymentId__isnull=False).values_list('paymentId')
                payments = Payment.objects.filter(id__in=paid_reservations, refundDate__isnull=True).update(refundDate=delete_date)

                reservations.update(cancellationDate=delete_date, stateId=state)

            serializer.save()

            return JsonResponse(data=serializer.data, status=201)

        return JsonResponse(status=400)