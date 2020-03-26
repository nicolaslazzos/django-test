from django.urls import path

from .views import ProvinceCreateListView, ProvinceIdListView, ProvinceNameListView

urlpatterns = [
    path('', ProvinceCreateListView.as_view(), name='province-create-list'),
    path('id/', ProvinceIdListView.as_view(), name='province-read-id'),
    path('name/', ProvinceNameListView.as_view(), name='province-read-name')
]