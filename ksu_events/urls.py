from django.urls import path
from .views import HomeView, ViewModelsView, CreateModelsView, EditEventView

'''Sets the home and models urls'''
urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('models/', ViewModelsView.as_view(), name="view_models"),
    path('orgdash/', CreateModelsView.as_view(), name="org_view"),
    path('edit/<int:event_id>/', EditEventView.as_view(), name='edit_event'),
]