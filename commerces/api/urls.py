from django.urls import path

from .views import CommerceListAPIView, CommerceCreateUpdateAPIView, CommerceRetrieveAPIView, CommerceDeleteAPIView

urlpatterns = [
    path('', CommerceListAPIView.as_view(), name='commerce-list'),
    path('create/', CommerceCreateUpdateAPIView.as_view(), name='commerce-create'),
    path('delete/<commerceId>', CommerceDeleteAPIView.as_view(), name='commerce-delete'),
    path('update/<commerceId>/', CommerceCreateUpdateAPIView.as_view(), name='commerce-update'),
    path('<commerceId>/', CommerceRetrieveAPIView.as_view(), name='commerce-read'),
]
