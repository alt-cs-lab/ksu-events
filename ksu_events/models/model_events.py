from django.db import models

from ksu_events.models.mixins import TimeStampMixin

class EventManager(models.Manager):
    """
    """

'''This is the event model it has 5 fields'''
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
