# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Local
from .models import Event, SubEvent, User

# This determines what information is on the django admin panel
class CASUserAdmin(UserAdmin):
    fieldsets = (
        ('Basic info', {'fields': ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'auth_role', 'is_superuser')}),
        ('Other info', {
            'fields': ('is_active', 'is_staff', 'groups', 'user_permissions'),
        }),
        ('Timestamps', {'fields': ('last_login', 'date_joined')}),
    )

    #overrides default save behaviour
    def save_model(self, request, obj, form, change):
        if not obj.password:
            obj.set_unusable_password()
        super().save_model(request, obj, form, change)

# Registered models.
admin.site.register(User, CASUserAdmin)
admin.site.register(Event)
admin.site.register(SubEvent)
