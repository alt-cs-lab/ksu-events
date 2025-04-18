from django.contrib import admin

from ksu_events.registration.models import Registrations, EthnicityOption

admin.site.register(EthnicityOption)
admin.site.register(Registrations)
