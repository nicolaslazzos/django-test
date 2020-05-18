from django.urls import path

from employees.api.views import RoleListAPIView, RoleIdListAPIView, EmployeeListAPIView, EmployeeCreateUpdateAPIView, EmployeeRetrieveAPIView, EmployeeDeleteAPIView

urlpatterns = [
  path('', EmployeeListAPIView.as_view(), name='employees-list'),
  path('roles/', RoleListAPIView.as_view(), name='roles-list'),
  path('roles/id/', RoleIdListAPIView.as_view(), name='roles-id-list'),
  path('create/', EmployeeCreateUpdateAPIView.as_view(), name='employee-create'),
  path('update/<id>/', EmployeeCreateUpdateAPIView.as_view(), name='employee-update'),
  path('delete/<id>/', EmployeeDeleteAPIView.as_view(), name='employee-delete'),
  path('<id>/', EmployeeRetrieveAPIView.as_view(), name='employee-read'),
]
