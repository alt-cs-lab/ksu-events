from django.db import models

from hackkstate.models.mixins import TimeStampMixin
from registration.models import Registrations


class Coach(TimeStampMixin, models.Model):

    registration_id = models.ForeignKey(Registrations, models.DO_NOTHING)
    affiliation = models.CharField(max_length=255, verbose_name='Affiliation')
    profession = models.CharField(max_length=255, verbose_name='Profession')
    verified = models.BooleanField(default=False, verbose_name='Verified')

    def __str__(self):
        return f"{self.affiliation} - {self.profession} - {'Verified' if self.verified else 'Not Verified'}"