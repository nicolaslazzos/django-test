from django.contrib import admin

from schedules.models import Schedule, Day, WorkShift

admin.site.register(Schedule)
admin.site.register(Day)
admin.site.register(WorkShift)