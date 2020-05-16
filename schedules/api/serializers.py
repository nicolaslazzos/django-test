from rest_framework import serializers

from schedules.models import Schedule, Day, WorkShift
from employees.api.serializers import EmployeeReadSerializer


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
    employee = EmployeeReadSerializer(read_only=True, source='employeeId')
    
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
