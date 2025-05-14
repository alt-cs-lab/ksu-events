#Django
from django.urls import path

# Local
from ksu_events.registration.views import EventRegistrationView

urlpatterns = [
    path('register/', EventRegistrationView.as_view(), name='register_event'),
]