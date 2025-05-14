# Django
from django import forms
from django.forms import ModelForm

# Local
from .models import Event, SubEvent

# This form is used to create or update Event instances using Django's ModelForm
class EventForm(ModelForm):
    # The form is based on the Event model
    class Meta:
        model = Event
        fields = ["name", "start_date", "end_date", "registration_start", "registration_end", "location"]
        
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'   

# This form is used to create or update subevent instances using Django's ModelForm            
class SubEventForm(ModelForm):
    # The form is based on the subevent model
    class Meta:
        model = SubEvent
        fields = ["name", "start_date", "end_date", "location"]
        
    def __init__(self, *args, **kwargs):
        super(SubEventForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'   
			