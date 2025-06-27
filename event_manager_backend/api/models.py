from django.db import models


# PUBLIC_INTERFACE
class Event(models.Model):
    """
    Represents an event for the event manager system.

    Fields:
        name (str): Name of the event.
        description (str): Description of the event.
        location (str): Where the event is held.
        start_time (datetime): When the event starts.
        end_time (datetime): When the event ends.
        created_at (datetime): Timestamp of event creation (auto).
        updated_at (datetime): Timestamp of event update (auto).
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
