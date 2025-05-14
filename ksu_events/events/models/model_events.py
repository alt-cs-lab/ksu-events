# Third-party
from django.db import models
from django.core.exceptions import ValidationError

# Local
from ksu_events.events.models.mixins import TimeStampMixin

class EventManager(models.Manager):
    """
    """

#This is our event class that contains 5 fields.  
# This event class is designed to allow a organiser to set up a large event for users to register too.
class Event(TimeStampMixin, models.Model):
    name = models.CharField(max_length=255, unique=True)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    registration_start = models.DateTimeField()
    registration_end = models.DateTimeField()
    location = models.CharField(max_length=500, default='')

    # custom object manager
    objects = EventManager()

    def __str__(self):
        return str(self.name)
    def toObj(self):
        return { 'id': self.pk, 
                 'updated_at': str(self.updated_at)
        }
    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)
    def clean(self):
        super().clean()
        if self.start_date >= self.end_date or self.registration_start >= self.registration_end:
            raise ValidationError("Start date must be before end date.")
