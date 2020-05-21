from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from django.db import transaction
from django.http import JsonResponse

from commerces.models import Commerce, Area
from employees.models import Employee, Role
from courts.models import Court
from schedules.models import Schedule, WorkShift, Day, Month
from profiles.models import Profile
from reservations.models import Reservation

from .serializers import CommerceSerializer, CommerceSerializer, AreaSerializer, AreaIdSerializer

import datetime
from collections import OrderedDict 


# COMMERCES

class CommerceListAPIView(generics.ListAPIView):
    serializer_class = CommerceSerializer

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


class CommerceCreateAPIView(generics.CreateAPIView):
    serializer_class = CommerceSerializer

    def get_queryset(self):
        return Commerce.objects.filter(softDelete__isnull=True)
        
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            commerce = serializer.save()
            
            profileId = request.data['profileId']
            profile = Profile.objects.get(id=profileId)
            profile.commerceId = commerce
            profile.save()

            role = Role.objects.get(id='OWNER')

            employee = Employee(profileId=profile, commerceId=commerce, roleId=role, inviteDate=datetime.datetime.now(), startDate=datetime.datetime.now())
            employee.save()

            return JsonResponse(data={ 'commerceId': commerce.id, 'employeeId': employee.id }, status=201)

        return JsonResponse(data='wrong parameters', status=400, safe=False)


class CommerceRetrieveUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView, generics.RetrieveAPIView):
    serializer_class = CommerceSerializer
    lookup_url_kwarg = 'commerceId'

    def get_queryset(self):
        return Commerce.objects.filter(softDelete__isnull=True)

    # def delete(self, request, pk):
    #     commerce_object = Commerce.objects.get(commerceId=pk)
    #     delete_date = datetime.datetime.now()
    #     serializer = self.serializer_class(commerce_object, data={ 'softDelete': delete_date }, partial=True)

    #     if serializer.is_valid():
    #         serializer.save()
    #         Employee.objects.filter(softDelete__isnull=True, commerceId=pk).update(softDelete=delete_date)
    #         Courts.objects.filter(softDelete__isnull=True, commerceId=pk).update(softDelete=delete_date)
    #         schedules = Schedule.objects.filter(softDelete__isnull=True, commerceId=pk)
    #         schedules.update(softDelete=delete_date)
    #         WorkShift.objects.filter(softDelete__isnull=True, scheduleId__in=schedules).update(softDelete=delete_date)
    #         Profile.objects.filter(softDelete__isnull=True, commerceId=pk).update(commerceId=None)
            
    #         return JsonResponse(code=201, data=serializer.data)

    #     return JsonResponse(code=400, data="wrong parameters")

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



# REPORTS

class CommerceDailyReservationsAPIView(APIView):
    def is_param_valid(self, param):
        return param != '' and param is not None

    def get(self, request, format=None):
        qs = Reservation.objects.filter(cancellationDate__isnull=True)

        commerceId = request.query_params.get('commerceId', None)
        employeeId = request.query_params.get('employeeId', None)
        startDate = request.query_params.get('startDate', None)
        endDate = request.query_params.get('endDate', None)

        if self.is_param_valid(commerceId):
            qs = qs.filter(commerceId=commerceId)

        if self.is_param_valid(employeeId):
            qs = qs.filter(employeeId=employeeId)

        if self.is_param_valid(startDate):
            qs = qs.filter(startDate__gte=startDate)
            
        if self.is_param_valid(endDate):
            qs = qs.filter(endDate__lte=endDate)

        days = Day.objects.all().order_by('id')
        days_labels = [day.name for day in days]

        reservations_count = [0] * 7

        for reservation in qs:
            weekday = reservation.startDate.isoweekday()
            if weekday == 7:
                weekday = 0
            reservations_count[weekday] += 1

        content = { 'labels': days_labels, 'data': reservations_count }

        return Response(content)


class CommerceYearsOfActivityAPIView(APIView):
    def is_param_valid(self, param):
        return param != '' and param is not None

    def get(self, request, format=None):
        qs = Reservation.objects.filter(cancellationDate__isnull=True).order_by('startDate')

        commerceId = request.query_params.get('commerceId', None)

        if self.is_param_valid(commerceId):
            qs = qs.filter(commerceId=commerceId)

        first_reservation = qs.first()
        current_year = datetime.datetime.now().year

        if first_reservation is not None:
            first_reservation_year = first_reservation.startDate.year
        else:
            first_reservation_year = current_year

        years_of_activity = []

        while first_reservation_year <= current_year:
            years_of_activity.append({ 'label': str(first_reservation_year), 'value': str(first_reservation_year) })
            first_reservation_year += 1

        content = { 'years': years_of_activity, 'selectedYear': str(current_year) }

        return Response(content)


class CommerceMonthlyEarningsAPIView(APIView):
    def is_param_valid(self, param):
        return param != '' and param is not None

    def get(self, request, format=None):
        qs = Reservation.objects.filter(cancellationDate__isnull=True, stateId='paid')

        commerceId = request.query_params.get('commerceId', None)
        employeeId = request.query_params.get('employeeId', None)
        year = request.query_params.get('year', None)

        if self.is_param_valid(commerceId):
            qs = qs.filter(commerceId=commerceId)

        if self.is_param_valid(employeeId):
            qs = qs.filter(employeeId=employeeId)

        if self.is_param_valid(year):
            startDate = datetime.date(int(year), 1, 1)
            endDate = datetime.date(int(year), 12, 31)
            qs = qs.filter(startDate__gte=startDate, startDate__lt=endDate)

        months = Month.objects.all().order_by('id')
        months_labels = [month.name for month in months]

        earnings_sum = [0] * 12

        for reservation in qs:
            earnings_sum[reservation.startDate.month - 1] += reservation.price

        content = { 'labels': months_labels, 'data': earnings_sum }

        return Response(content)


class CommerceMonthlyReviewsAPIView(APIView):
    def is_param_valid(self, param):
        return param != '' and param is not None

    def get(self, request, format=None):
        qs = Reservation.objects.filter(cancellationDate__isnull=True, stateId='paid')

        commerceId = request.query_params.get('commerceId', None)
        employeeId = request.query_params.get('employeeId', None)
        year = request.query_params.get('year', None)

        if self.is_param_valid(commerceId):
            qs = qs.filter(commerceId=commerceId)

        if self.is_param_valid(employeeId):
            qs = qs.filter(employeeId=employeeId)

        if self.is_param_valid(year):
            startDate = datetime.date(int(year), 1, 1)
            endDate = datetime.date(int(year), 12, 31)
            qs = qs.filter(startDate__gte=startDate, startDate__lt=endDate)

        months = Month.objects.all().order_by('id')
        months_labels = [month.name for month in months]

        reviews_sum = [0] * 12
        reviews_count = [0] * 12

        for reservation in qs:
            if reservation.clientReviewId is not None:
                reviews_sum[reservation.startDate.month - 1] += reservation.clientReviewId.rating
                reviews_count[reservation.startDate.month - 1] += 1

        reviews_avg = [reviews_sum[i] / reviews_count[i] if reviews_count[i] else 0 for i in range(len(reviews_sum))]

        content = { 'labels': months_labels, 'data': reviews_avg }

        return Response(content)


class CommerceReservedAndCanceledReservationsAPIView(APIView):
    def is_param_valid(self, param):
        return param != '' and param is not None

    def get(self, request, format=None):
        qs = Reservation.objects.all()

        commerceId = request.query_params.get('commerceId', None)
        employeeId = request.query_params.get('employeeId', None)
        startDate = request.query_params.get('startDate', None)
        endDate = request.query_params.get('endDate', None)

        if self.is_param_valid(commerceId):
            qs = qs.filter(commerceId=commerceId)

        if self.is_param_valid(employeeId):
            qs = qs.filter(employeeId=employeeId)

        if self.is_param_valid(startDate):
            qs = qs.filter(startDate__gte=startDate)
            
        if self.is_param_valid(endDate):
            qs = qs.filter(endDate__lte=endDate)

        state_labels = ['Realizados', 'Cancelados']
        reservations_count = [
            qs.exclude(stateId='canceled').count(),
            qs.filter(stateId='canceled').count(),
        ]

        content = { 'labels': state_labels, 'data': reservations_count }

        return Response(content)


class CommerceMostPopularShiftsAPIView(APIView):
    def is_param_valid(self, param):
        return param != '' and param is not None

    def get(self, request, format=None):
        qs = Reservation.objects.filter(cancellationDate__isnull=True)

        commerceId = request.query_params.get('commerceId', None)
        employeeId = request.query_params.get('employeeId', None)
        startDate = request.query_params.get('startDate', None)
        endDate = request.query_params.get('endDate', None)

        if self.is_param_valid(commerceId):
            qs = qs.filter(commerceId=commerceId)

        if self.is_param_valid(employeeId):
            qs = qs.filter(employeeId=employeeId)

        if self.is_param_valid(startDate):
            qs = qs.filter(startDate__gte=startDate)
            
        if self.is_param_valid(endDate):
            qs = qs.filter(endDate__lte=endDate)

        shifts_count = OrderedDict() 

        for reservation in qs:
            shift = reservation.startDate.strftime("%H:%M")
            shifts_count[shift] = shifts_count.get(shift, 0) + 1

        labels = shifts_count.keys() if len(shifts_count.keys()) else ['Sin Datos']
        data = shifts_count.values() if len(shifts_count.values()) else [0]

        content = { 'labels': labels, 'data': data }

        return Response(content)