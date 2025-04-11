from django import forms
from django.forms import ModelForm

from .models import Event, EventAttendance, Registration

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["name", "start_date", "end_date", "registration_start", "registration_end", "location"]

class EventAttendanceForm(forms.ModelForm):
    event = forms.ModelChoiceField(queryset=Event.objects.all(), empty_label="Select an event")

    class Meta:
        model = Registration
        fields = ['event']