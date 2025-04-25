from django import forms

from ksu_events.events.models import Event
from ksu_events.registration.models import Registrations


class RegistrationForm(forms.ModelForm):
    event = forms.ModelChoiceField(
        queryset=Event.objects.all(), 
        empty_label="Select an event",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Registrations
        fields = [
            'event', 
            'country', 
            'dietary_restrictions', 
            'phone_number',
            'ethnicity',
            'is_minor',
            'participation',
            'shirt_size',
            'year_in_school'
        ]
        # Exclude the user field since we'll set it automatically
        exclude = ['user']
        
        widgets = {
            'country': forms.Select(attrs={'class': 'form-control'}),
            'dietary_restrictions': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'ethnicity': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'is_minor': forms.BooleanField(attrs={'class': 'form-control'}),
            'participation': forms.Select(attrs={'class': 'form-control'}),
            'shirt_size': forms.Select(attrs={'class': 'form-control'}),
            'year_in_school': forms.Select(attrs={'class': 'form-control'}),
        }