from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from ksu_events.models.model_users import User

class OrganizerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.auth_role == User.AuthLevel.ORGANIZER

    def handle_no_permission(self):
        return HttpResponseForbidden("You do not have permission to access this page.")