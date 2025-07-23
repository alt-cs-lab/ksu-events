from django.contrib import admin

from student_events.registration.models import Registrations, EthnicityOption

admin.site.register(EthnicityOption)
admin.site.register(Registrations)
