from rest_framework import generics

from notifications.models import NotificationToken, Notification
from employees.models import Employee
from notifications.api.serializers import NotificationTokenSerializer, NotificationSerializer


class NotificationTokenListAPIView(generics.ListAPIView):
    serializer_class = NotificationTokenSerializer

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = NotificationToken.objects.all()

        profileId = self.request.query_params.get('profileId', None)
        commerceId = self.request.query_params.get('commerceId', None)
        employeeId = self.request.query_params.get('employeeId', None)

        if self.is_param_valid(profileId):
            qs = qs.filter(profileId=profileId)

        if self.is_param_valid(commerceId):
            employees_profiles = Employee.objects.filter(softDelete__isnull=True, commerceId=commerceId).values_list('profileId')
            qs = qs.filter(profileId__in=employees_profiles)

        if self.is_param_valid(employeeId):
            employee = Employee.objects.filter(softDelete__isnull=True, employeeId=employeeId)
            qs = qs.filter(profileId=employee.profileId.id)

        return qs


class NotificationTokenCreateDestroyAPIView(generics.DestroyAPIView, generics.CreateAPIView):
    serializer_class = NotificationTokenSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return NotificationToken.objects.all()


class NotificationListAPIView(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def is_param_valid(self, param):
        return param != '' and param is not None

    def get_queryset(self):
        qs = Notification.objects.filter(softDelete__isnull=True)

        profileId = self.request.query_params.get('profileId', None)
        commerceId = self.request.query_params.get('commerceId', None)
        employeeId = self.request.query_params.get('employeeId', None)

        if self.is_param_valid(commerceId):
            qs = qs.filter(commerceId=commerceId)

        if self.is_param_valid(profileId):
            qs = qs.filter(profileId=profileId)

        if self.is_param_valid(employeeId):
            qs = qs.filter(employeeId=employeeId)

        return qs


class NotificationCreateRetrieveUpdateAPIView(generics.CreateAPIView, generics.UpdateAPIView, generics.RetrieveAPIView):
    serializer_class = NotificationSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Notification.objects.filter(softDelete__isnull=True)
