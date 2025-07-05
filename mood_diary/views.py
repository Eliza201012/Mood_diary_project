from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

def home(request):
    if request.method == "POST":
        mood_diary = Mood_diary()
        mood_diary.date = request.POST.get("date")
        mood_diary.mood = request.POST.get("mood")
        mood_diary.comment = request.POST.get("comment")
        mood_diary.save()
        return HttpResponseRedirect("/")
    entries = Mood_diary.objects.order_by("-date")
    return render(request, "home.html", {"entries" : entries})