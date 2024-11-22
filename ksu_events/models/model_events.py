from django.db import models

from ksu_events.models.mixins import TimeStampMixin

class EventManager(models.Manager):
    """
    """

class Event(TimeStampMixin, models.Model):
    name = models.CharField(max_length=255, unique=True)

    event_start_date = models.DateTimeField()
    event_end_date = models.DateTimeField()
    registration_start_date = models.DateTimeField()
    registration_end_date = models.DateTimeField()
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