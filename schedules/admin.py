from django.contrib import admin

from schedules.models import Schedule, Day, WorkShift

# Register your models here.
admin.site.register(Schedule)
admin.site.register(Day)
admin.site.register(WorkShift)