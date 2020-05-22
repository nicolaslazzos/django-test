from django.urls import path

from .views import ProfileListAPIView, ProfileCreateUpdateDestroyAPIView, ProfileRetrieveAPIView, ProfileWorkplacesListAPIView, FavoriteListAPIView, FavoriteIdListAPIView, FavoriteCreateDeleteAPIView

urlpatterns = [
    # PROFILES 
    path('profiles/', ProfileListAPIView.as_view(), name='profile-list'),
    path('profiles/create/', ProfileCreateUpdateDestroyAPIView.as_view(), name='profile-create'),
    path('profiles/update/<profileId>/', ProfileCreateUpdateDestroyAPIView.as_view(), name='profile-update'),
    path('profiles/delete/<profileId>/', ProfileCreateUpdateDestroyAPIView.as_view(), name='profile-delete'),
    path('profiles/<profileId>/', ProfileRetrieveAPIView.as_view(), name='profile-read'),
    # FAVORITES
    path('favorites/', FavoriteListAPIView.as_view(), name='favorite-list'),
    path('favorites/create/', FavoriteCreateDeleteAPIView.as_view(), name='favorite-create'),
    path('favorites/id/', FavoriteIdListAPIView.as_view(), name='favorite-id-list'),
    path('favorites/delete/<id>/', FavoriteCreateDeleteAPIView.as_view(), name='favorite-delete'),
    # WORKPLACES
    path('workplaces/', ProfileWorkplacesListAPIView.as_view(), name='profile-workplaces'),
]
