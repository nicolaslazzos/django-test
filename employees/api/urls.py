from django.urls import path

from employees.api.views import RoleListAPIView, RoleIdListAPIView, EmployeeListAPIView, EmployeeCreateRetrieveUpdateDestroyAPIView, EmployeeCreateRetrieveUpdateDestroyAPIView, EmployeeCreateRetrieveUpdateDestroyAPIView

urlpatterns = [
  path('', EmployeeListAPIView.as_view(), name='employees-list'),
  path('roles/', RoleListAPIView.as_view(), name='roles-list'),
  path('roles/id/', RoleIdListAPIView.as_view(), name='roles-id-list'),
  path('create/', EmployeeCreateRetrieveUpdateDestroyAPIView.as_view(), name='employee-create'),
  path('update/<id>/', EmployeeCreateRetrieveUpdateDestroyAPIView.as_view(), name='employee-update'),
  path('delete/<id>/', EmployeeCreateRetrieveUpdateDestroyAPIView.as_view(), name='employee-delete'),
  path('<id>/', EmployeeCreateRetrieveUpdateDestroyAPIView.as_view(), name='employee-read'),
]
