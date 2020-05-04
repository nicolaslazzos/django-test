from django.urls import path

from .views import ServiceListAPIView, ServiceCreateRetrieveUpdateAPIView

urlpatterns = [
  path('', ServiceListAPIView.as_view(), name='services-list'),
  path('create/', ServiceCreateRetrieveUpdateAPIView.as_view(), name='service-create'),
  path('update/<id>/', ServiceCreateRetrieveUpdateAPIView.as_view(), name='services-update'),
  path('<id>/', ServiceCreateRetrieveUpdateAPIView.as_view(), name='service-read'),
]