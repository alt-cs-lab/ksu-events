from django.urls import path
from .views import home, view_models, UserProfileView

'''Sets the home and models urls'''
urlpatterns = [
    path('', home, name='home_view'),
    path('models/', view_models, name="models_view"),
    path("profile/", UserProfileView.as_view(), name="user-profile")
]
