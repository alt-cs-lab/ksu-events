# Standard library
from datetime import datetime

# Third-party
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from ksu_events.events.models.mixins import TimeStampMixin
from ksu_events.events.models.model_events import Event

# restricts what the date should look like
def validate_date_format(value):
    try:
        datetime.strptime(value, '%m-%d-%Y')
    except ValueError:
        raise ValidationError('Date of Birth must be in MM-DD-YYYY format')

# This is our User class which is mainly used for determining the auth level of our users.
# Users with the Org Role have the most Permissions and can access much more of the sight.
# There are three major fields d.o.b., auth_role, and email
class User(AbstractUser, TimeStampMixin):
    date_of_birth = models.DateField(
        null=True, blank=False, verbose_name='Date of Birth', help_text='MM-DD-YYYY')

    # event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    # institution = models.CharField(max_length=255, blank=True)
    # team = models.CharField(max_length=255, blank=True)
    
    class AuthLevel(models.TextChoices):
        ORGANIZER = 'ORG', _('Organizer')
        VOLUNTEER = 'VOL', _('Volunteer')
        PARTICIPANT = 'PAR', _('Participant') 

    auth_role = models.CharField(max_length=3, choices=AuthLevel.choices, default=AuthLevel.PARTICIPANT, blank=False)
    email = models.EmailField(_("email address"), blank=True)
    # is_organizer = models.BooleanField(default=False)

    """This class extends the base Django Auth User model to allow for additional fields"""

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f"{self.username} {self.email}"

    class Meta:
        swappable = "AUTH_USER_MODEL"