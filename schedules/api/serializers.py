from rest_framework import serializers

from schedules.models import Schedule, Day, WorkShift

class WorkShiftSerializer(serializers.ModelSerializer):
  class Meta:
    model = WorkShift
    fields = [
      'id',
      'days',
      'firstShiftStart',
      'firstShiftEnd',
      'secondShiftStart',
      'secondShiftEnd'
    ]
    read_only_fields = ['id']

class ScheduleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Schedule
    fields = [
      'id',
      'commerceId',
      # 'employeeId',
      'startDate',
      'endDate'      
    ]