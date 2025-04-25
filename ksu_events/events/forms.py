from django import forms
from django.forms import ModelForm

from .models import Event, SubEvent

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["name", "start_date", "end_date", "registration_start", "registration_end", "location"]
        
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'   

class SubEventForm(ModelForm):
    class Meta:
        model = SubEvent
        fields = ["name", "start_date", "end_date", "location"]
        
    def __init__(self, *args, **kwargs):
        super(SubEventForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'   