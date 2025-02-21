from django.urls import path
<<<<<<< Updated upstream
from .views import home, view_models, UserProfileView
=======
from ksu_events.views.other_views import HomeView, ViewModelsView, CreateModelsView, EditEventView, UserProfileView
>>>>>>> Stashed changes

'''Sets the home and models urls'''
urlpatterns = [
    path('', home, name='home_view'),
    path('models/', view_models, name="models_view"),
    path("profile/", UserProfileView.as_view(), name="user-profile")
]
