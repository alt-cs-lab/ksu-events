# Third-party
from django.db import models

# Local
from ksu_events.events.models.mixins import TimeStampMixin
from ksu_events.events.models.model_events import Event

# Our sub-event contains 5 fields and is designed to split up events into multiple parts.
# The splitting up of events is primarily done to help illistrate what will be occuring during the events of the day
# TODO add sub-event attendance at some point
class SubEvent(TimeStampMixin, models.Model):
    
    name = models.CharField(max_length=500, unique=True)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=True, blank=True)

    location = models.CharField(max_length=500, default='') 

    def __str__(self):
        return '{}-{}'.format(self.pk, self.name)

    class Meta: 
        unique_together = (("name", "event"))