from django.urls import path

from schedules.api.views import ScheduleListAPIView, ScheduleCreateUpdateDestroyAPIView, WorkShiftListAPIView, WorkShiftCreateUpdateAPIView, ScheduleSettingListAPIView, ScheduleSettingCreateUpdateAPIView

urlpatterns = [
  path('', ScheduleListAPIView.as_view(), name='schedules-list'),
  path('create/', ScheduleCreateUpdateDestroyAPIView.as_view(), name='schedule-create'),
  path('settings/', ScheduleSettingListAPIView.as_view(), name='schedule-settings-list'),
  path('settings/create/', ScheduleSettingCreateUpdateAPIView.as_view(), name='schedule-setting-create'),
  path('settings/update/<id>/', ScheduleSettingCreateUpdateAPIView.as_view(), name='schedule-setting-update'),
  path('workshifts/', WorkShiftListAPIView.as_view(), name='workshifts-list'),
  path('workshifts/create/', WorkShiftCreateUpdateAPIView.as_view(), name='workshift-create'),
  path('workshifts/update/<id>', WorkShiftCreateUpdateAPIView.as_view(), name='workshift-update'),
  path('update/<id>/', ScheduleCreateUpdateDestroyAPIView.as_view(), name='schedule-update'),
  path('delete/<id>/', ScheduleCreateUpdateDestroyAPIView.as_view(), name='schedule-update'),
]