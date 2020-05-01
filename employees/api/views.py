from rest_framework import generics

from employees.models import Role, Employee
from employees.api.serializers import RoleSerializer, EmployeeReadSerializer, EmployeeCreateUpdateSerializer


class RoleListAPIView(generics.ListAPIView):
    serializer_class = RoleSerializer

    def get_queryset(self):
        return Role.objects.filter(softDelete__isnull=True)


class EmployeeListAPIView(generics.ListAPIView):
    serializer_class = EmployeeReadSerializer

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = Employee.objects.filter(softDelete__isnull=True)

        commerceId = self.request.query_params.get('commerceId', None)
        profileId = self.request.query_params.get('profileId', None)

        if self.is_param_valid(commerceId):
            qs = qs.filter(commerceId=commerceId)

        if self.is_param_valid(profileId):
            qs = qs.filter(profileId=profileId)

        return qs


class EmployeeRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = EmployeeReadSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Employee.objects.filter(softDelete__isnull=True)


class EmployeeCreateUpdateAPIView(generics.CreateAPIView, generics.UpdateAPIView):
    serializer_class = EmployeeCreateUpdateSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Employee.objects.filter(softDelete__isnull=True)
