from django.urls import path

from employees.api.views import RoleListAPIView, EmployeeListAPIView, EmployeeCreateUpdateAPIView, EmployeeRetrieveAPIView

urlpatterns = [
  path('', EmployeeListAPIView.as_view(), name='employees-list'),
  path('roles/', RoleListAPIView.as_view(), name='roles-list'),
  path('create/', EmployeeCreateUpdateAPIView.as_view(), name='employee-create'),
  path('update/<id>/', EmployeeCreateUpdateAPIView.as_view(), name='employee-update'),
  path('<id>/', EmployeeRetrieveAPIView.as_view(), name='employee-read'),
]
