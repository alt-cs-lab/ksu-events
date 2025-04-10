from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.shortcuts import get_object_or_404, redirect

from ksu_events.models import Event
from ksu_events.registration.models.model_registration import Registrations
from ksu_events.registration.forms import RegistrationForm


class RegisterView(LoginRequiredMixin, FormView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'

    def dispatch(self, request, *args, **kwargs):
        self.event = get_object_or_404(Event, id=kwargs['event_id'])
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form

    def form_valid(self, form):
        existing = Registrations.objects.filter(user=self.request.user, event=self.event).first()
        if existing:
            return redirect('already_registered')

        registration = form.save(commit=False)
        registration.user = self.request.user
        registration.event = self.event
        registration.save()
        form.save_m2m()
        return redirect('registration_success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = self.event
        return context