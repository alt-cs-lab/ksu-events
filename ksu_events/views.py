from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return HttpResponse("Hello world, this msg is from the events pkg")


@login_required
def redirect(request):
    user = request.user
    username = user.username

    return HttpResponse(username + " has successfully logged in with KSU CAS Auth.")
