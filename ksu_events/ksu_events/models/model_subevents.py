from django.db import models
from ksu_events.ksu_events.models.mixins import TimeStampMixin
from ksu_events.ksu_events.models.model_events import Event

class SubEvent(TimeStampMixin, models.Model):
    
    subevent_name = models.CharField(max_length=500, unique=True)
    parent_event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    
    subevent_start_date = models.DateTimeField(null=False, blank=False)
    subevent_end_date = models.DateTimeField(null=True, blank=True)

    location = models.CharField(max_length=500, blank=False) 

    def __str__(self):
        return '{}-{}'.format(self.pk, self.subevent_name)

    class Meta: 
        unique_together = (("subevent_name", "parent_event"))