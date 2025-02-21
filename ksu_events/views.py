from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
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

@login_required
def create_models(request):
    try:
        if request.method == 'POST':
            form = EventForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('organizer_dash')
        else:
            form = EventForm()
        return render(request, 'ksu_events/organizer_dash.html', {'form': form})
    except Exception as e:  #Horrible fix please fix asap
        event_models = Event.objects.all()

        context = {
            'event_models': event_models
        }

        return render(request, 'ksu_events/view_models.html', context)
    

@login_required
def edit_event(request, event_id=None):
    try:
        if event_id:  
            event = get_object_or_404(Event, id=event_id)
        else:  
            event = None

        form = EventForm(request.POST or None, instance=event)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect('view_models')

        return render(request, 'ksu_events/edit_event.html', {'form': form})
    except Exception as e: #Horrible fix please change asap
        event_models = Event.objects.all()

        context = {
            'event_models': event_models
        }

        return render(request, 'ksu_events/view_models.html', context)

'''This method shows that a user has logged in'''
@login_required
def redirect(request):
    user = request.user
    username = user.username
    
    return HttpResponse(username + " has successfully logged in with KSU CAS Auth.")
    