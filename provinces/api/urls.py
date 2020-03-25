from django.urls import path

from .views import ProvinceCreateListView, ProvinceIdListView, ProvinceNameListView

urlpatterns = [
    path('', ProvinceCreateListView.as_view(), name='province-create'),
    path('id/', ProvinceIdListView.as_view(), name='province-rid'),
    path('name/', ProvinceNameListView.as_view(), name='province-rname')
]