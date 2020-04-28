from django.urls import path

from schedules.api.views import ScheduleListAPIView, ScheduleCreateUpdateAPIView, WorkShiftListAPIView, WorkShiftCreateUpdateView

urlpatterns = [
  path('', ScheduleListAPIView.as_view(), name='schedules-list'),
  path('create/', ScheduleCreateUpdateAPIView.as_view(), name='schedule-create'),
  path('workshifts/', WorkShiftListAPIView.as_view(), name='workshifts-list'),
  path('workshifts/create/', WorkShiftCreateUpdateView.as_view(), name='workshift-create'),
  path('update/<id>/', ScheduleCreateUpdateAPIView.as_view(), name='schedule-update'),
  path('workshifts/update/<id>', WorkShiftCreateUpdateView.as_view(), name='workshift-update'),
]