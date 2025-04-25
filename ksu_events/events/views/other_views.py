from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from ksu_events.events.models import Event, SubEvent
from ksu_events.events.forms import EventForm, SubEventForm
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
    
    def form_invalid(self, form):
        context = {
            'event_models': Event.objects.all()
        }
        return render(self.request, 'ksu_events/view_models.html', context)
    
class CreateSubEventView(OrganizerRequiredMixin, CreateView):
    model = SubEvent
    form_class = SubEventForm
    template_name = 'ksu_events/create_subevent.html'
    
    def dispatch(self, request, *args, **kwargs):
        print("kwargs =", self.kwargs)
        self.event = get_object_or_404(Event, pk=self.kwargs['event_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.parent_event = self.event
        return super().form_valid(form)

    def form_invalid(self, form):
        context = {
            'event_models': Event.objects.all()
        }
        return render(self.request, 'ksu_events/view_models.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = self.event
        return context

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

    