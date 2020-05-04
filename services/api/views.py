from rest_framework import generics

from .serializers import ServiceSerializer

from services.models import Service


class ServiceListAPIView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = Service.objects.filter(softDelete__isnull=True).order_by('name')

        commerceId = self.request.query_params.get('commerceId', None)
        employeeId = self.request.query_params.get('employeeId', None)
        
        if self.is_param_valid(commerceId):
            qs = qs.filter(commerceId=commerceId)

        if self.is_param_valid(employeeId):
            qs = qs.filter(employeesIds=employeeId)

        return qs


class ServiceCreateRetrieveUpdateAPIView(generics.CreateAPIView, generics.RetrieveAPIView, generics.UpdateAPIView):
    serializer_class = ServiceSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Service.objects.filter(softDelete__isnull=True)
