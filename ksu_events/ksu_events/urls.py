from django.urls import path
from ksu_events.ksu_events import views

urlpatterns = [
    path('', views.home, name='home_view'),
]