from django.urls import path

from .views import AreaCreateListView, AreaIdListView

urlpatterns = [
    path('', AreaCreateListView.as_view(), name='province-create-list'),
    path('id/', AreaIdListView.as_view(), name='province-read-id')
]