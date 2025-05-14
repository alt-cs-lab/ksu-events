# Django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib import messages

#Local
from ksu_events.registration.models.model_registrations import Registrations
from ksu_events.registration.forms import RegistrationForm

# Register.html
# model_registrations.py & model_ethnicity_options.py
# This is the view that allows users to register for events 
class EventRegistrationView(LoginRequiredMixin, CreateView):
    model = Registrations
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home_view')
    
    def form_valid(self, form):
        # Get the selected event from the cleaned form data
        event = form.cleaned_data['event']
        # Check if the user is already registered for the event
        existing_registration = Registrations.objects.filter(
            user=self.request.user,
            event=event
        ).exists()
        
        if existing_registration:
            # Add a message to inform the user
            messages.warning(self.request, f"You are already registered for {event}.")
            return redirect(self.success_url)
        form.instance.user = self.request.user
        return super().form_valid(form)