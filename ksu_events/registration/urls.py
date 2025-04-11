from django.urls import path, include


urlpatterns = [
    path('register/', EventRegistrationView.as_view(), name='register_event'),
]