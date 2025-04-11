from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.shortcuts import get_object_or_404, redirect

from ksu_events.events.models import Event
from ksu_events.registration.models.model_registration import Registrations
from ksu_events.registration.forms import RegistrationForm
from django.contrib import messages
from ksu_events.registration.models import Registration

class EventRegistrationView(LoginRequiredMixin, CreateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'ksu_events/register.html'
    success_url = reverse_lazy('home_view')
    
    def form_valid(self, form):
        event = form.cleaned_data['event']
        existing_registration = Registration.objects.filter(
            user=self.request.user,
            event=event
        ).exists()
        
        if existing_registration:
            # Add a message to inform the user
            messages.warning(self.request, f"You are already registered for {event}.")
            return redirect(self.success_url)
        form.instance.user = self.request.user
        return super().form_valid(form)