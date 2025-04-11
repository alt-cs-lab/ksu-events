from django.urls import path, include
from ksu_events.registration.views import EventRegistrationView


urlpatterns = [
    path('register/', EventRegistrationView.as_view(), name='register_event'),
]