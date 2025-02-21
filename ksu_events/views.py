from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm
from datetime import datetime


class HomeView(TemplateView):
    template_name = 'ksu_events/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().replace(tzinfo=None)
        events = Event.objects.order_by('event_start_date')
        
        for event in events:
            if event.event_end_date.replace(tzinfo=None) >= today:
                context['event_start_date'] = event.event_start_date
                break
        
        return context


class ViewModelsView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'ksu_events/view_models.html'
    context_object_name = 'event_models'

class CreateModelsView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'ksu_events/organizer_dash.html'
    success_url = reverse_lazy('organizer_dash')
    
    def form_invalid(self, form):
        context = {
            'event_models': Event.objects.all()
        }
        return render(self.request, 'ksu_events/view_models.html', context)
    

class EditEventView(LoginRequiredMixin, UpdateView):
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

class RedirectView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        username = request.user.username
        return HttpResponse(f"{username} has successfully logged in with KSU CAS Auth.")

    