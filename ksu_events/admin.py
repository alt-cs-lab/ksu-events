from django.contrib import admin
from .models import Event, SubEvent, EthnicityOption, MajorOption, Registrations

# Registered models.
admin.site.register(Event)
admin.site.register(SubEvent)
admin.site.register(EthnicityOption)
admin.site.register(MajorOption)
admin.site.register(Registrations)