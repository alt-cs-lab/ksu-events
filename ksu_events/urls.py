from django.urls import path
from .views import home, view_models, create_models, edit_event

'''Sets the home and models urls'''
urlpatterns = [
    path('', home, name='home_view'),
    path('models/', view_models, name="models_view"),
    path('orgdash/', create_models, name="org_view"),
    path('orgdash/<int:event_id>/', edit_event, name='orgdash'),
]