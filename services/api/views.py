from rest_framework import generics
from django.http import JsonResponse

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

        return qs.order_by('name')


class ServiceCreateRetrieveUpdateAPIView(generics.CreateAPIView, generics.RetrieveAPIView, generics.UpdateAPIView):
    serializer_class = ServiceSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Service.objects.filter(softDelete__isnull=True)

    def service_name_exists(self, id, name, commerceId):
        qs = self.get_queryset().filter(name=name, commerceId=commerceId)

        if id is not None:
            qs = qs.exclude(id=id)

        return qs.count() >= 1

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        commerceId = request.data['commerceId']
        name = request.data['name']

        if self.service_name_exists(None, name, commerceId):
            return JsonResponse(data={ 'on_service_exists': True })

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(data=serializer.data, status=201)

        return JsonResponse(status=400)

    def update(self, request, id, *args, **kwargs):
        service = Service.objects.get(id=id)
        serializer = self.serializer_class(service, data=request.data, partial=True)

        name = request.data['name']
        commerceId = service.commerceId.id

        if self.service_name_exists(id, name, commerceId):
            return JsonResponse(data={ 'on_service_exists': True })

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(data=serializer.data, status=201)

        return JsonResponse(status=400)