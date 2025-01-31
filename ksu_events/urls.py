from django.urls import path
from .views import home, view_models, org_models

'''Sets the home and models urls'''
urlpatterns = [
    path('', home, name='home_view'),
    path('models/', view_models, name="models_view"),
    path('models/', org_models, name="org_view"),
]