from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import *

def home(request):
    mood_diary = Mood_diary.objects.all()
    return render(request, "home.html", {"mood_diary" : mood_diary})

def create(request):
    if request.method == "POST":
        mood_diary = Mood_diary()
        mood_diary.date = request.POST.get("date")
        mood_diary.mood = request.POST.get("mood")
        mood_diary.comment = request.POST.get("comment")
        mood_diary.save()
        return HttpResponseRedirect("/")
    entries = Mood_diary.objects.order_by("-date")
    return render(request, "home.html", {"entries" : entries})

def edit(request, id):
    try:
        mood_diary = Mood_diary.objects.get(id=id)
        if request.method == "POST":
            mood_diary.date = request.POST.get("date")
            mood_diary.mood = request.POST.get("mood")
            mood_diary.comment = request.POST.get("comment")
            mood_diary.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"mood_diary" : mood_diary})
    except Mood_diary.DoesNotExist:
        return HttpResponseNotFound("<h2>Your entry was not found</h2>")
    
def delete(request, id):
    try:
        mood_diary = Mood_diary.objects.get(id=id)
        mood_diary.delete()
        return HttpResponseRedirect("/")
    except Mood_diary.DoesNotExist:
        return HttpResponseNotFound("<h2>Your entry was not found</h2>")