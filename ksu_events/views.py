from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Event


def home(request): 
    return render(request, 'ksu_events/home_page.html')
    #return HttpResponse("Hello world, this msg is from the events pkg")

def view_models(request):
    event_models = Event.objects.all()

    context = {
        'event_models': event_models
    }

    return render(request, 'ksu_events/view_models.html', context)


@login_required
def redirect(request):
    user = request.user
    username = user.username
    
    return HttpResponse(username + " has successfully logged in with KSU CAS Auth.")
    