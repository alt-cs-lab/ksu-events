from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _

from ksu_events.models.mixins import TimeStampMixin
from ksu_events.models.model_events import Event


def validate_date_format(value):
    try:
        datetime.strptime(value, '%m-%d-%Y')
    except ValueError:
        raise ValidationError('Date of Birth must be in MM-DD-YYYY format')


class User(AbstractUser, TimeStampMixin):
    date_of_birth = models.DateField(
        null=True, blank=False, verbose_name='Date of Birth', help_text='MM-DD-YYYY')

    # event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    # institution = models.CharField(max_length=255, blank=True)
    # team = models.CharField(max_length=255, blank=True)
    
    #class AuthLevel(models.TextChoices):
    #    ORGANIZER = 'ORG', _('Organizer')
    #    VOLUNTEER = 'VOL', _('Volunteer')
    #    PARTICIPANT = 'PAR', _('Participant') 

    # auth_role = models.CharField(max_length=3, choices=AuthLevel.choices, default=AuthLevel.ORGANIZER, blank=False)
    # is_organizer = models.BooleanField(default=False)

    """This class extends the base Django Auth User model to allow for additional fields"""

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f"{self.email}"

    class Meta:
        swappable = "AUTH_USER_MODEL"