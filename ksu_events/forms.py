from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["name", "event_start_date", "event_end_date", "registration_start_date", "registration_end_date", "location"]