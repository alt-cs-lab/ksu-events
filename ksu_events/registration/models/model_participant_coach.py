from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps

from ksu_events.models.mixins import TimeStampMixin

class ParticipantCoach(TimeStampMixin, models.Model):
    participant = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='participant_coach', verbose_name='Participant')
    coach = models.ForeignKey('registration.Coach', on_delete=models.CASCADE, related_name='coached_participants', verbose_name='Coach')
    verified = models.BooleanField(default=False, verbose_name='Verified')

    def __str__(self):
        return f"{self.participant.get_full_name()} - {self.coach.affiliation}"

    class Meta:
        unique_together = ('participant', 'coach')
