from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    mood_diary = Mood_diary.objects.all()
    return render(request, "home.html", {"mood_diary" : mood_diary})