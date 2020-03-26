from django.urls import path

from .views import ProfileListAPIView, ProfileCreateUpdateAPIView, ProfileRetrieveAPIView

urlpatterns = [
    path('', ProfileListAPIView.as_view(), name='profile-list'),
    path('<clientId>/', ProfileRetrieveAPIView.as_view(), name='profile-read'),
    path('create/', ProfileCreateUpdateAPIView.as_view(), name='profile-create'),
    path('update/<clientId>/', ProfileCreateUpdateAPIView.as_view(), name='profile-update')
]
