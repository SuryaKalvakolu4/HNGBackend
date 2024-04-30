from django.db import models
from challenges.models import Instructor


class Event(models.Model):
    day = models.CharField(max_length=100, verbose_name="Challenge day")
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    link = models.URLField(verbose_name="Link to the event")
    name = models.CharField(max_length=100, verbose_name="Event name")
    requirements = models.CharField(max_length=100)
    instructor = models.ManyToManyField(Instructor, blank=True)
    image = models.URLField(verbose_name="Link to the image")
    
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self) -> str:
        return self.day
