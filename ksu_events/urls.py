from django.urls import path
from ksu_events.views.other_views import HomeView, ViewModelsView, CreateModelsView, EditEventView, UserProfileView, ViewParticipantsView, EventAttendanceView

# Sets the home and models urls
urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('models/', ViewModelsView.as_view(), name="view_models"),
    path('orgdash/', CreateModelsView.as_view(), name="organizer_dash"),
    path('edit/<int:event_id>/', EditEventView.as_view(), name='edit_event'),
    path("profile/", UserProfileView.as_view(), name="user-profile"),
    path('register/', EventAttendanceView.as_view(), name='attend_event'),
    path('participants', ViewParticipantsView.as_view(), name="participants")
]
