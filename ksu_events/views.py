from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm
from datetime import datetime


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

@login_required
def create_models(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organizer_dash')
    else:
        form = EventForm()
    return render(request, 'ksu_events/organizer_dash.html', {'form': form})

@login_required
def edit_event(request, event_id=None):
    if event_id:  
        event = get_object_or_404(Event, id=event_id)
    else:  
        event = None

    form = EventForm(request.POST or None, instance=event)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('view_models')

    return render(request, 'ksu_events/edit_event.html', {'form': form})

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        event.delete()  
        return redirect('view_models')  

    return render(request, 'ksu_events/view_models.html', {'event': event})

'''This method shows that a user has logged in'''
@login_required
def redirect(request):
    user = request.user
    username = user.username
    
    return HttpResponse(username + " has successfully logged in with KSU CAS Auth.")
    