from django.urls import path
from .views import home, view_models

urlpatterns = [
    path('', home, name='home_view'),
    path('/models', view_models, name="models_view"),
]