from django.conf import settings
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="events"
    )
    guests = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="guest_events", blank=True
    )

    def __str__(self):
        return self.title
