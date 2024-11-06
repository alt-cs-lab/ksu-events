from django.db import models
from django.core.exceptions import ValidationError

from base.models.mixins import TimeStampMixin

class EventManager(models.manager):
    def get_active_season(self):
        active_season = self.get_active_season_qurey()
        if active_season:
            return active_season.season
        else: 
            return None
        
    def get_active_season_query(self):
        result = self.filter(status='active').first()
        if result:
            return result.get()
        return None

class Event(TimeStampMixin, models.Model):
    name = models.CharField(max_length=255, unique=True)
    season = models.CharField(max_length=8, verbose_name="Event Season")

    event_start_date = models.DateTimeField()
    event_end_date = models.DateTimeField()
    registration_start_date = models.DateTimeField()
    registration_end_date = models.DateTimeField()
    location = models.CharField(max_length=500, default='')

    # active flag
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('active', 'Active'),
        ('completed', 'Completed')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='upcoming')

    # custom object manager
    objects = EventManager()

    def __str__(self):
        return ''.join([self.pk])
    def toObj(self):
        return { 'id': self.pk, 
                 'season': self.season,
                 'status': self.status,
                 'updated_at': str(self.updated_at)
        }
    def save(self, *args, **kwargs):
        if self.status == 'active':
            if Event.objects.filter(status='active').exclude(pk=self.pk).exists():
                raise ValidationError('There can only be one active event at a time')
        super().save(*args, **kwargs)