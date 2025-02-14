from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Event
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "user_profile.html"
    context_object_name = "user_profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["user_fields"] = vars(user)
        return context



'''This home method tells the urls.py what to display.  The html page but also the closest start date for the next event.'''
def home(request): 
    i = 1
    event = Event.objects.order_by('event_start_date').first()
    today = datetime.now().replace(tzinfo=None)

    '''Checks if event exists'''
    if event:
        '''if end date has passed check the next up coming event if not next event then we render without input'''
        while event.event_end_date.replace(tzinfo=None) < today:
            try:
                event = Event.objects.order_by('event_start_date').all()[i]
                i+=1
            except IndexError:
                return render(request, 'ksu_events/home_page.html')
        return render(request, 'ksu_events/home_page.html', {'event_start_date': event.event_start_date})
    else:
        return render(request, 'ksu_events/home_page.html')
    #return HttpResponse("Hello world, this msg is from the events pkg")

'''This view_models method tells the urls.py what to display specifically the model page html file'''
def view_models(request):
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
    