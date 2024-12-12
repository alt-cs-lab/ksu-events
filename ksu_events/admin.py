from django.contrib import admin
from .models import Event, SubEvent

# Registered models.
admin.site.register(Event)
admin.site.register(SubEvent)
