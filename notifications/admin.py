from django.contrib import admin

from notifications.models import NotificationToken, NotificationType, Notification


admin.site.register(NotificationToken)
admin.site.register(NotificationType)
admin.site.register(Notification)
