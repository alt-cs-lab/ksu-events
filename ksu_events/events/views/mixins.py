# Django
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

# Local
from ksu_events.events.models.model_users import User

# This mixin makes it so when put in the arguments of views it requires an organizer to access
class OrganizerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.auth_role == User.AuthLevel.ORGANIZER

    def handle_no_permission(self):
        return redirect('/')