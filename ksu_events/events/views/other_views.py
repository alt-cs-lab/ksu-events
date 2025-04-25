from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from ksu_events.events.models import Event, SubEvent
from ksu_events.events.forms import EventForm, SubEventForm
from ksu_events.registration.models.model_registrations import Registrations
from ksu_events.events.views.mixins import OrganizerRequiredMixin
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "ksu_events/user_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["user_profile"] = user
        context["hidden_fields"] = ["password", "id", "password", "is_superuser","is_staff", "is_active", "created_at", "updated_at", "date_of_birth"]
        context["user_fields"] = {
            field.name: getattr(user, field.name) for field in User._meta.get_fields() if not field.is_relation
        }

        return context



class HomeView(TemplateView):
    template_name = 'ksu_events/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().replace(tzinfo=None)
        events = Event.objects.order_by('start_date')
        if events.exists():
            i = 0
            event = events[i]
            '''if end date has passed check the next up coming event if not next event then we render without input'''
            while event.end_date.replace(tzinfo=None) < today:
                i+=1
                try:
                    event = events[i]
                except IndexError:
                    context['clock_end_time'] = None
                    return context
            context['clock_end_time'] = event.start_date
        else:
            context['clock_end_time'] = None  # No events in database
        return context


class ViewModelsView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'ksu_events/view_models.html'
    context_object_name = 'event_models'

class CreateModelsView(OrganizerRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'ksu_events/organizer_dash.html'
    success_url = reverse_lazy('organizer_dash')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event_models'] = Event.objects.all()  # Filter active events

        # Get the selected event ID from the query parameters
        selected_event_id = self.request.GET.get('selected_event_id')
        print(f"Selected Event ID: {selected_event_id}")  # Debugging line
        if selected_event_id and selected_event_id != -1:
            selected_event = Event.objects.filter(id=selected_event_id).first()
            context['selected_event'] = selected_event
            if selected_event:
                # Get the registrations for the selected event
                user_list = Registrations.objects.filter(event=selected_event).select_related('user')
                print(f"User List: {user_list}")  # Debugging line
                context['registered_users'] = user_list
        else:
            context['selected_event'] = None  # Default to None if no event is selected
            context['registered_users'] = []

        return context
    
    def form_invalid(self, form):
        context = {
            'event_models': Event.objects.all(),
            'registrations_models': Registrations.objects,
            'selected_event': None
        }
        return render(self.request, 'ksu_events/view_models.html', context)
    

class EditEventView(OrganizerRequiredMixin,  UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'ksu_events/edit_event.html'
    success_url = reverse_lazy('view_models')
    
    def get_object(self, queryset=None):
        event_id = self.kwargs.get('event_id')
        return get_object_or_404(Event, id=event_id)
    
    def form_invalid(self, form):
        context = {
            'event_models': Event.objects.all()
        }
        return render(self.request, 'ksu_events/view_models.html', context)
    
class AddSubeventView(OrganizerRequiredMixin, CreateView):
    model = SubEvent
    form_class = SubEventForm
    template_name = 'ksu_events/add_subevent.html'
    success_url = reverse_lazy('view_models')
    
    def form_valid(self, form):
        event_id = self.kwargs.get('event_id')
        event = get_object_or_404(Event, id=event_id)
        form.instance.event = event
        return super().form_valid(form)
    
    def form_invalid(self, form):
        context = {
            'subevent_models': SubEvent.objects.all()
        }
        return render(self.request, 'ksu_events/view_models.html', context)

class ViewSubEventsView(LoginRequiredMixin, ListView):
    model = SubEvent
    template_name = 'ksu_events/view_subevents.html'
    context_object_name = 'subevent_models'

    def get_queryset(self):
        event_id = self.kwargs.get('event_id')
        return SubEvent.objects.filter(event_id=event_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_id = self.kwargs.get('event_id')
        context['event'] = Event.objects.get(id=event_id)
        return context

class EditSubEventView(LoginRequiredMixin, UpdateView):
    model = SubEvent
    form_class = SubEventForm
    template_name = 'ksu_events/edit_subevent.html'
    pk_url_kwarg = 'subevent_id'
    
    def get_success_url(self):
        return reverse_lazy('view_subevents', kwargs={'event_id': self.kwargs['event_id']})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_id = self.kwargs.get('event_id')
        context['event'] = Event.objects.get(id=event_id)
        return context

class ViewParticipantsView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'ksu_events/view_participant.html'
    context_object_name = 'users'

    #def get_queryset(self):
        #return User.objects.filter(auth_role='PAR')

class RedirectView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        username = request.user.username
        return HttpResponse(f"{username} has successfully logged in with KSU CAS Auth.")

    