from django.db import models
import json

from ksu_events.models import Event
from ksu_events.models.mixins import TimeStampMixin

class EventAttendance(TimeStampMixin, models.Model):
    registration = # models.ForeignKey(Registrations, blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("regisration", "created_at"),)

    def toObj(self):
        return {'id': self.pk, 'eventID': self.eventID.pk, 'user': self.registration.user.pk, 'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)}
    
    @staticmethod
    def attendance_count(registration, event):
        return EventAttendance.objects.filter(registration=registration, eventID=event).count()
