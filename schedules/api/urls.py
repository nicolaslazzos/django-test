from django.urls import path

from schedules.api.views import ScheduleListAPIView, ScheduleCreateUpdateDestroyAPIView, WorkShiftListAPIView, WorkShiftCreateUpdateAPIView

urlpatterns = [
  path('', ScheduleListAPIView.as_view(), name='schedules-list'),
  path('create/', ScheduleCreateUpdateDestroyAPIView.as_view(), name='schedule-create'),
  path('workshifts/', WorkShiftListAPIView.as_view(), name='workshifts-list'),
  path('workshifts/create/', WorkShiftCreateUpdateAPIView.as_view(), name='workshift-create'),
  path('update/<id>/', ScheduleCreateUpdateDestroyAPIView.as_view(), name='schedule-update'),
  path('delete/<id>/', ScheduleCreateUpdateDestroyAPIView.as_view(), name='schedule-update'),
  path('workshifts/update/<id>', WorkShiftCreateUpdateAPIView.as_view(), name='workshift-update'),
]