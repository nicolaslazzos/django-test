from django.urls import path

from notifications.api.views import NotificationTokenListAPIView, NotificationTokenCreateDestroyAPIView, NotificationListAPIView, NotificationCreateRetrieveUpdateAPIView

urlpatterns = [
  path('tokens/delete/<id>/', NotificationTokenCreateDestroyAPIView.as_view(), name='notification-tokens-delete'),
  path('tokens/create/', NotificationTokenCreateDestroyAPIView.as_view(), name='notification-tokens-create'),
  path('tokens/', NotificationTokenListAPIView.as_view(), name='notification-tokens-list'),
  path('update/<id>/', NotificationCreateRetrieveUpdateAPIView.as_view(), name='notification-update'),
  path('create/', NotificationCreateRetrieveUpdateAPIView.as_view(), name='notification-create'),
  path('<id>/', NotificationCreateRetrieveUpdateAPIView.as_view(), name='notification-read'),
  path('', NotificationListAPIView.as_view(), name='notifications-list'),
]