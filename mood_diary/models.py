from django.db import models

class Mood_diary(models.Model):
    MOOD_OPTIONS = [
        ("happy", "Щасливий"),
        ("sad", "Сумний"),
        ("angry", "Злий"),
        ("neutral", "Нейтральний"),
        ("Idgaf", "На все пофіг")
    ]
    date = models.DateField()
    mood = models.CharField(max_length=20, choices=MOOD_OPTIONS, default="Undefined")
    comment = models.TextField(max_length=200)