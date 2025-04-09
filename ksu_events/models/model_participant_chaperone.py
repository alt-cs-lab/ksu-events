from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps

from ksu_events.models.mixins import TimeStampMixin
from ksu_events.models.model_chaperone import Chaperone

class ParticipantChaperone(TimeStampMixin, models.Model):
    participant = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='participant_chaperone', verbose_name='Participant')
    chaperone = models.ForeignKey(Chaperone, on_delete=models.CASCADE, related_name='chaperoned_participants', verbose_name='Chaperone')
    verified = models.BooleanField(default=False, verbose_name='Verified')

    def __str__(self):
        return f"{self.participant.get_full_name()} - {self.chaperone.affiliation}"

    class Meta:
        unique_together = ('participant', 'chaperone')