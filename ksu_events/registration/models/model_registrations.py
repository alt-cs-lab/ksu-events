"""
This class adds a profile linked to a user who is registered. Currently, the
userprofile is linked to the user model through a one-to-one relationship and is used
for registration for the hackathon for the current season.
"""
# Standard Library
import os
from datetime import datetime

# Django
from django.db import models

# Third-Party
from django_countries.fields import CountryField
from simple_history.models import HistoricalRecords

# Local
from ksu_events.events.models.mixins import TimeStampMixin
from ksu_events.events.models.model_events import Event
from ksu_events.events.models.model_users import User
from ksu_events.registration.models.model_ethnicity_options import EthnicityOption

# Optional (commented out): SocialAccount from allauth
# from allauth.socialaccount.models import SocialAccount

# Custom manager for Registrations model
class RegistrationProfileManager(models.Manager):
    def get_registration_event(self, user, event_id):
        return Registrations.objects.get(user=user, event_id=event_id)

    def get_registrations(self, user):
        return Registrations.objects.get(user=user)

# Registration model for users participating in events
# This model contains all the fields that are seen in the registration html file
class Registrations(TimeStampMixin, models.Model):
    """This class adds a profile linked to a user who is registered"""

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)

    country = CountryField(blank=True, blank_label='(select country)')
    dietary_restrictions = models.TextField(max_length=250, default='', blank=True, null=True,
                                            verbose_name='Do you have any dietary restrictions?')
    phone_number = models.CharField(max_length=15, blank=True, null=False)
    ethnicity = models.ManyToManyField(EthnicityOption)
    is_minor = models.BooleanField(default=False, verbose_name='Under 18')

    PARTICIPATION_CHOICES = [
        ('N/A', 'Not Sure'),
        ('ONL', 'Online'),
        ('INP', 'In-person'),
    ]
    participation = models.CharField(max_length=4, blank=False, null=False,
                                     choices=PARTICIPATION_CHOICES,
                                     default='INP',
                                     verbose_name="How do you plan to participate in this event?")

    SHIRT_CHOICES = [
        ('EXS', 'X-Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'X-Large'),
        ('XXL', 'XX-Large'),
    ]
    shirt_size = models.CharField(max_length=4, blank=False, null=False, choices=SHIRT_CHOICES,
                                  verbose_name="Shirt Size")
    
    YEAR_IN_SCHOOL_CHOICES = [
        ('HSFR', 'High School Freshman'),
        ('HSSO', 'High School Sophomore'),
        ('HSJR', 'High School Junior'),
        ('HSSR', 'High School Senior'),
        ('CFR', 'College Freshman'),
        ('CSO', 'College Sophomore'),
        ('CJR', 'College Junior'),
        ('CSR', 'College Senior'),
        ('COLD', 'College 5th year or greater'),
        ('NTRD', 'Nontraditional Student'),
        ('GRDS', 'Graduate Student'),
        ('VOCA', 'Other Vocational / Trade Program or Apprenticeship'),
        ('NO', 'I prefer not to answer'),
    ]
    year_in_school = models.CharField(max_length=4, blank=False, null=False,
                                      choices=YEAR_IN_SCHOOL_CHOICES,
                                      verbose_name="Education Level")

    history = HistoricalRecords()
    objects = RegistrationProfileManager()

    def __str__(self):
        return f"{self.user}-{self.user.email}"
    
    def get_reg_info(self):
        return {
            'username': self.user,
            'name': self.user.full_name(),
            'email': self.user.email,
            'country': self.country,
            'dietary_restrictions': self.dietary_restrictions,
            'phone_number': self.phone_number,
            'shirt_size': self.shirt_size,
            'year_in_school': self.year_in_school,
            'participation': self.participation,
            'is_minor': self.is_minor
        }

    # Ensure one registration per user per event
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'event'], name='cnst_unique_userEvent')
        ]
