from rest_framework import generics
from django.db.models import Q

from commerces.models import Commerce, Area
from employees.models import Employee
from courts.models import Court
from schedules.models import Schedule, WorkShift
from profiles.models import Profile

from .serializers import CommerceReadSerializer, CommerceCreateUpdateSerializer, AreaSerializer, AreaIdSerializer

import datetime


# COMMERCES

class CommerceListAPIView(generics.ListAPIView):
    serializer_class = CommerceReadSerializer

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = Commerce.objects.filter(softDelete__isnull=True)

        areaId = self.request.query_params.get('areaId', None)
        provinceId = self.request.query_params.get('provinceId', None)
        userSearch = self.request.query_params.get('contains', None)
        cuit = self.request.query_params.get('cuit', None)

        if self.is_param_valid(areaId):
            qs = qs.filter(areaId=areaId)

        if self.is_param_valid(provinceId):
            qs = qs.filter(provinceId=provinceId)

        if self.is_param_valid(userSearch):
            qs = qs.filter(Q(name__icontains=userSearch) | Q(description__icontains=userSearch))
            
        if self.is_param_valid(cuit):
            qs = qs.filter(cuit=cuit)

        return qs.order_by('name')


class CommerceCreateUpdateAPIView(generics.CreateAPIView, generics.UpdateAPIView):
    lookup_url_kwarg = 'commerceId'
    serializer_class = CommerceCreateUpdateSerializer

    def get_queryset(self):
        return Commerce.objects.filter(softDelete__isnull=True)
        
    # def patch(self, request, pk, *args, **kwargs):
    #     rating = self.request.POST.get('rating', None)

    #     if rating is not None:
    #         commerce_object = Commerce.objects.get(commerceId=pk)
    #         serializer = self.serializer_class(
    #             commerce_object, 
    #             data={ 'ratingCount': commerce_object.ratingCount + 1, 'ratingTotal': commerce_object.ratingTotal + rating }, 
    #             partial=True
    #         )
    #     else:
    #         serializer = self.serializer_class(data=request.data, partial=True)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(code=201, data=serializer.data)

    #     return JsonResponse(code=400, data="wrong parameters")

        

class CommerceDeleteAPIView(generics.DestroyAPIView):
    lookup_url_kwarg = 'commerceId'
    serializer_class = CommerceCreateUpdateSerializer

    def get_queryset(self):
        return Commerce.objects.filter(softDelete__isnull=True)

    def delete(self, request, pk):
        commerce_object = Commerce.objects.get(commerceId=pk)
        delete_date = datetime.datetime.now()
        serializer = self.serializer_class(commerce_object, data={ 'softDelete': delete_date }, partial=True)

        if serializer.is_valid():
            serializer.save()
            Employee.objects.filter(softDelete__isnull=True, commerceId=pk).update(softDelete=delete_date)
            Courts.objects.filter(softDelete__isnull=True, commerceId=pk).update(softDelete=delete_date)
            schedules = Schedule.objects.filter(softDelete__isnull=True, commerceId=pk)
            schedules.update(softDelete=delete_date)
            WorkShift.objects.filter(softDelete__isnull=True, scheduleId__in=schedules).update(softDelete=delete_date)
            Profile.objects.filter(softDelete__isnull=True, commerceId=pk).update(commerceId=None)
            
            return JsonResponse(code=201, data=serializer.data)

        return JsonResponse(code=400, data="wrong parameters")


class CommerceRetrieveAPIView(generics.RetrieveAPIView):
    lookup_url_kwarg = 'commerceId'
    serializer_class = CommerceReadSerializer

    def get_queryset(self):
        return Commerce.objects.filter(softDelete__isnull=True)


# AREAS

class AreaListAPIView(generics.ListAPIView):
  serializer_class = AreaSerializer
  
  def get_queryset(self):
    qs = Area.objects.all()
    return qs.filter(softDelete__isnull=True).order_by('name')


class AreaIdListAPIView(generics.ListAPIView):
  serializer_class = AreaIdSerializer
  
  def get_queryset(self):
    qs = Area.objects.all()
    return qs.filter(softDelete__isnull=True).order_by('name')