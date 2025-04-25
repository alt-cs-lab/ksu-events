from django.db import models
from ksu_events.events.models.mixins import TimeStampMixin
from ksu_events.events.models.model_events import Event

'''This is the event model it has 5 fields and helps split up the event in theory'''
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