from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Event, SubEvent, User

class CASUserAdmin(UserAdmin):
    # Override save_model to make password field optional
    def save_model(self, request, obj, form, change):
        # Don't require a password when saving
        if not obj.password:
            obj.set_unusable_password()
        super().save_model(request, obj, form, change)

# Registered models.
admin.site.register(User, CASUserAdmin)
admin.site.register(Event)
admin.site.register(SubEvent)
