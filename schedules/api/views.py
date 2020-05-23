from rest_framework import generics
from django.db.models import Q

from schedules.models import Schedule, WorkShift, Day, ScheduleSetting
from schedules.api.serializers import WorkShiftSerializer, ScheduleSerializer, ScheduleSettingSerializer


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


class ScheduleCreateUpdateDestroyAPIView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = ScheduleSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Schedule.objects.filter(softDelete__isnull=True)


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
