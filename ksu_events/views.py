from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Event


def home(request, event_id): 
    event = Event.objects.get(pk=event_id)
    return render(request, 'ksu_events/home_page.html', {'event_start_date': event.event_start_date})
    #return HttpResponse("Hello world, this msg is from the events pkg")


@login_required
def redirect(request):
    user = request.user
    username = user.username
    
    return HttpResponse(username + " has successfully logged in with KSU CAS Auth.")