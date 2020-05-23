from rest_framework import serializers

from schedules.models import Schedule, Day, WorkShift, ScheduleSetting
from employees.api.serializers import EmployeeSerializer


class WorkShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkShift
        fields = [
            'id',
            'scheduleId',
            'days',
            'firstShiftStart',
            'firstShiftEnd',
            'secondShiftStart',
            'secondShiftEnd'
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'scheduleId': {'write_only': True}
        }


class ScheduleSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True, source='employeeId')
    
    class Meta:
        model = Schedule
        fields = [
            'id',
            'commerceId',
            'employee',
            'employeeId',
            'startDate',
            'endDate',
            'reservationMinLength'
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'commerceId': {'write_only': True}
        }


class ScheduleSettingSerializer(serializers.ModelSerializer):
    scheduleSettingId = serializers.IntegerField(read_only=True, source='id')

    class Meta:
        model = ScheduleSetting
        fields = ['scheduleSettingId', 'commerceId', 'employeeId', 'reservationDayPeriod', 'reservationMinCancelTime']
        extra_kwargs = {
            'commerceId': { 'write_only': True },
            'employeeId': { 'write_only': True },
        }