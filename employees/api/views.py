from rest_framework import generics

from employees.models import Role, Employee
from schedules.models import Schedule, WorkShift
from employees.api.serializers import RoleSerializer, RoleIdSerializer, EmployeeReadSerializer, EmployeeCreateUpdateSerializer


class RoleListAPIView(generics.ListAPIView):
    serializer_class = RoleSerializer

    def get_queryset(self):
        return Role.objects.filter(softDelete__isnull=True).order_by('name')


class RoleIdListAPIView(generics.ListAPIView):
    serializer_class = RoleIdSerializer

    def get_queryset(self):
        return Role.objects.filter(softDelete__isnull=True).order_by('name')


class EmployeeListAPIView(generics.ListAPIView):
    serializer_class = EmployeeReadSerializer

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = Employee.objects.filter(softDelete__isnull=True)

        commerceId = self.request.query_params.get('commerceId', None)
        profileId = self.request.query_params.get('profileId', None)
        startDate = self.request.query_params.get('startDate', None)
        visible = self.request.query_params.get('visible', None)
        employeesIds = self.request.query_params.get('employeesIds', None)

        if self.is_param_valid(commerceId):
            qs = qs.filter(commerceId=commerceId)

        if self.is_param_valid(profileId):
            qs = qs.filter(profileId=profileId)

        if self.is_param_valid(startDate):
            qs = qs.filter(startDate__isnull=False)

        if self.is_param_valid(visible):
            qs = qs.filter(visible=True)

        if self.is_param_valid(employeesIds):
            qs = qs.filter(id__in=employeesIds)

        return qs.order_by('profileId__firstName', 'profileId__lastName')


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

class EmployeeDeleteAPIView(generics.DestroyAPIView):
    serializer_class = EmployeeCreateUpdateSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Employee.objects.filter(softDelete__isnull=True)

    def delete(self, request, pk):
        employee_object = Employee.objects.get(id=pk)
        delete_date = datetime.datetime.now()
        serializer = self.serializer_class(employee_object, data={ 'softDelete': delete_date }, partial=True)

        if serializer.is_valid():
            serializer.save()
            schedules = Schedule.objects.filter(softDelete__isnull=True, employeeId=pk)
            schedules.update(softDelete=delete_date)
            WorkShift.objects.filter(softDelete__isnull=True, scheduleId__in=schedules).update(softDelete=delete_date)

            return JsonResponse(code=201, data=serializer.data)

        return JsonResponse(code=400, data="wrong parameters")