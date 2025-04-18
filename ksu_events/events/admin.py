from django.contrib import admin
from .models import Event, SubEvent, User

# Registered models.
admin.site.register(Event)
admin.site.register(SubEvent)
admin.site.register(User)
