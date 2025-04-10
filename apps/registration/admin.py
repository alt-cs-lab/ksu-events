import csv

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

#from registration.forms.form_user import CustomUserCreationForm, CustomUserChangeForm
from registration.models import Registrations, MajorOption, EthnicityOption
from ksu_events.models.model_users import User
#from ksu_events.util.mixins import ExportCsvMixin, EmailSelectedMixin
from simple_history.admin import SimpleHistoryAdmin

"""
# Define a new User admin
class UserAdmin(BaseUserAdmin, ExportCsvMixin, EmailSelectedMixin):
    model = User
    verbose_name_plural = 'users'
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = (
        'email', 'first_name', 'last_name', 'updated_at')
    search_fields = ('email',)
    ordering = ('updated_at', 'email',)
    filter_horizontal = ()
    actions = ["export_as_csv", 'bulk_email_users', 'email_individuals']
    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if request.user.username[0].upper() != 'J':
    #         if 'delete_selected' in actions:
    #             del actions['delete_selected']
    #     return actions


# TODO: Rename and update to match the Registrations model
class UserProfileAdmin(SimpleHistoryAdmin, ExportCsvMixin, EmailSelectedMixin):
    model = Registrations
    verbose_name_plural = 'users'
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = (
        'user', 'first_name', 'last_name', 'is_minor',
        'all_ethnicities', 'year_in_school', 'all_majors', 'country',
        'updated_at', 'mlh_communication', 'shirt_size', 'dietary_restrictions',
    )
    search_fields = ['user__email', 'participation', 'user__first_name', 'user__last_name']
    list_filter = ('year_in_school', 'hackathon_id')
    actions = ["export_as_csv", 'bulk_email_users', 'email_individuals']
    ordering = ('-updated_at', 'user',)
    filter_horizontal = ()

    def first_name(self, instance):  # name of the method should be same as the field given in `list_display`
        try:
            return instance.registration.first_name
        except:
            return 'ERROR!!'

    def last_name(self, instance):  # name of the method should be same as the field given in `list_display`
        try:
            return instance.registration.last_name
        except:
            return 'ERROR!!'


    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if request.user.username[0].upper() != 'J':
    #         if 'delete_selected' in actions:
    #             del actions['delete_selected']
    #     return actions
"""


admin.site.register(EthnicityOption)
admin.site.register(MajorOption)
admin.site.register(Registrations)
