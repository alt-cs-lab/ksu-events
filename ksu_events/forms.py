from django import forms
from django.forms import ModelForm

from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["name", "start_date", "end_date", "registration_start", "registration_end", "location"]