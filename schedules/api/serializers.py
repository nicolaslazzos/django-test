from rest_framework import serializers

from schedules.models import Schedule, Day, WorkShift


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
    class Meta:
        model = Schedule
        fields = [
            'id',
            'commerceId',
            'employeeId',
            'startDate',
            'endDate',
            'reservationMinLength'
        ]
        extra_kwargs = {
            'commerceId': {'write_only': True}
        }
