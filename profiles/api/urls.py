from django.urls import path

from .views import ProfileRetrieveUpdateView, ProfileCreateListView

urlpatterns = [
    path('', ProfileCreateListView.as_view(), name='profile-create'),
    path('<clientId>/', ProfileRetrieveUpdateView.as_view(), name='profile-ru')
]
