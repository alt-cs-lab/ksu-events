# Standard library
import json

# Third-party
from django.db import models

# Local
from ksu_events.events.models import Event
from ksu_events.events.models.mixins import TimeStampMixin
from ksu_events.registration.models.model_registrations import Registrations

#This class is not used yet so for the next year the idea behind this is that when someone registers for an event this will be used to see if they have attended a sub-event 
class EventAttendance(TimeStampMixin, models.Model):
    registration = models.ForeignKey(Registrations, blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("registration", "created_at"),)

    def toObj(self):
        return {'id': self.pk, 'eventID': self.registration.event.pk, 'user': self.registration.user.pk, 'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)}
    
    @staticmethod
    def attendance_count(registration, event):
        return EventAttendance.objects.filter(registration=registration, eventID=event).count()
