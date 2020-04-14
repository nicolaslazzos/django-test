from django.urls import path

from .views import ProfileListAPIView, ProfileCreateUpdateAPIView, ProfileRetrieveAPIView, FavoriteListAPIView, FavoriteIdListAPIView, FavoriteCreateDeleteAPIView

urlpatterns = [
    # PROFILES
    path('profiles/', ProfileListAPIView.as_view(), name='profile-list'),
    path('profiles/<clientId>/', ProfileRetrieveAPIView.as_view(), name='profile-read'),
    path('profiles/create/', ProfileCreateUpdateAPIView.as_view(), name='profile-create'),
    path('profiles/update/<clientId>/', ProfileCreateUpdateAPIView.as_view(), name='profile-update'),
    # FAVORITES
    path('favorites/', FavoriteListAPIView.as_view(), name='favorite-list'),
    path('favorites/delete/<id>/', FavoriteCreateDeleteAPIView.as_view(), name='favorite-delete'),
    path('favorites/create/', FavoriteCreateDeleteAPIView.as_view(), name='favorite-create'),
    path('favorites/id/', FavoriteIdListAPIView.as_view(), name='favorite-id-list')
]
