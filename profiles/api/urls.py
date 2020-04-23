from django.urls import path

from .views import ProfileListAPIView, ProfileCreateUpdateAPIView, ProfileRetrieveAPIView, FavoriteListAPIView, FavoriteIdListAPIView, FavoriteCreateDeleteAPIView

urlpatterns = [
    # PROFILES 
    # importa el orden en el proceso de ver si la url coincide, por lo que en este caso profiles/<clientId> conviene que este despues de profiles/create
    # por ejemplo, ya que sino al hacer un post a la url profiles/create, si primero esta profiles/<clientId>, piensa que la palabra "create" es un clientId
    path('profiles/', ProfileListAPIView.as_view(), name='profile-list'),
    path('profiles/create/', ProfileCreateUpdateAPIView.as_view(), name='profile-create'),
    path('profiles/update/<clientId>/', ProfileCreateUpdateAPIView.as_view(), name='profile-update'),
    path('profiles/<clientId>/', ProfileRetrieveAPIView.as_view(), name='profile-read'),
    # FAVORITES
    path('favorites/', FavoriteListAPIView.as_view(), name='favorite-list'),
    path('favorites/create/', FavoriteCreateDeleteAPIView.as_view(), name='favorite-create'),
    path('favorites/id/', FavoriteIdListAPIView.as_view(), name='favorite-id-list'),
    path('favorites/delete/<id>/', FavoriteCreateDeleteAPIView.as_view(), name='favorite-delete'),
]
