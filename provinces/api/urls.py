from django.urls import path

from .views import ProvinceRetrieveUpdateView, ProvinceCreateListView

urlpatterns = [
    path('', ProvinceCreateListView.as_view(), name='province-create'),
    path('<pk>/', ProvinceRetrieveUpdateView.as_view(), name='province-ru')
]