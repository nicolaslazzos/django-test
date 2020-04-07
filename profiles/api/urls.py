from django.urls import path

from .views import ProfileListAPIView, ProfileCreateUpdateAPIView, ProfileRetrieveAPIView, FavoriteListAPIView, FavoriteCommerceIdListAPIView

urlpatterns = [
    # PROFILES
    path('profiles/', ProfileListAPIView.as_view(), name='profile-list'),
    path('profiles/<clientId>/', ProfileRetrieveAPIView.as_view(), name='profile-read'),
    path('profiles/create/', ProfileCreateUpdateAPIView.as_view(), name='profile-create'),
    path('profiles/update/<clientId>/', ProfileCreateUpdateAPIView.as_view(), name='profile-update'),
    # FAVORITES
    path('favorites/', FavoriteListAPIView.as_view(), name='favorite-list'),
    path('favorites/id/', FavoriteCommerceIdListAPIView.as_view(), name='favorite-id-list')
]
