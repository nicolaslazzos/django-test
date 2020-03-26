from django.urls import path

from .views import CommerceListAPIView, CommerceCreateUpdateAPIView, CommerceRetrieveAPIView

urlpatterns = [
    path('', CommerceListAPIView.as_view(), name='commerce-list'),
    path('<commerceId>/', CommerceRetrieveAPIView.as_view(), name='commerce-read'),
    path('create/', CommerceCreateUpdateAPIView.as_view(), name='commerce-create'),
    path('update/<commerceId>/', CommerceCreateUpdateAPIView.as_view(), name='commerce-update')
]
