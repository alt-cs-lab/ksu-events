from django.urls import path
from .views import HomeView, ViewModelsView, create_models, edit_event

'''Sets the home and models urls'''
urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('models/', ViewModelsView.as_view(), name="models_view"),
    path('orgdash/', create_models, name="org_view"),
    path('edit/<int:event_id>/', edit_event, name='edit_event'),
]