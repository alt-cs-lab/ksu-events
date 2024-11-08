from django.urls import path
from ksu_events.base import views

urlpatterns = [
    path('', views.home, name='home_view'),
]