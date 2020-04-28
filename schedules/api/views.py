from rest_framework import generics

from schedules.models import Schedule, WorkShift, Day
from schedules.api.serializers import WorkShiftSerializer, ScheduleSerializer


class ScheduleListAPIView(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = Schedule.objects.filter(softDelete=None)

        commerceId = self.request.query_params.get('commerceId', None)
        startDate = self.request.query_params.get('startDate', None)
        endDate = self.request.query_params.get('endDate', None)

        if self.is_param_valid(commerceId):
            qs = qs.filter(commerceId=commerceId)

        if self.is_param_valid(startDate):
            qs.filter(startDate__lte=startDate)

        if self.is_param_valid(startDate):
            qs.filter(endDate__gt=startDate)

        return qs


class ScheduleCreateUpdateAPIView(generics.CreateAPIView, generics.UpdateAPIView):
    serializer_class = ScheduleSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Schedule.objects.filter(softDelete=None)


class WorkShiftListAPIView(generics.ListAPIView):
    serializer_class = WorkShiftSerializer

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = WorkShift.objects.all()

        scheduleId = self.request.query_params.get('scheduleId', None)

        if self.is_param_valid(scheduleId):
            qs = qs.filter(scheduleId=scheduleId)

        return qs


class WorkShiftCreateUpdateView(generics.CreateAPIView, generics.UpdateAPIView):
    serializer_class = WorkShiftSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return WorkShift.objects.all()
