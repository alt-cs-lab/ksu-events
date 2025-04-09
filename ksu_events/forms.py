from django import forms
from django.forms import ModelForm
from django_countries.widgets import CountrySelectWidget

from .models import Event, Registrations

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["name", "start_date", "end_date", "registration_start", "registration_end", "location"]

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registrations
        exclude = ['user', 'event', 'history']  # user and event should probably be set in the view
        fields = [
            'ethnicity', 'country', 'year_in_school', 'shirt_size','dietary_restrictions',
            'phone_number', 'is_minor', 'participation']
        widgets = {
            'dietary_restrictions': forms.Textarea(attrs={'rows': 2, 'cols': 60}),
            'ethnicity': forms.CheckboxSelectMultiple(),
            'country': CountrySelectWidget()
        }