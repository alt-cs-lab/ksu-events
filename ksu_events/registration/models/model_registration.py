"""
This class adds a profile linked to a user who is registered. Currently, the
userprofile is linked to the user model through a one-to-one relationship and is used
for registration for the hackathon for the current season.
"""
import os
from datetime import datetime

#from allauth.socialaccount.models import SocialAccount
from django.core.exceptions import ValidationError
from django.db import models

from ksu_events.models.model_events import Event
from ksu_events.models.mixins import TimeStampMixin
from ksu_events.models.model_users import User
from ksu_events.registration.models.model_ethnicity_options import EthnicityOption

from django.dispatch import receiver
from simple_history.models import HistoricalRecords
from django_countries.fields import CountryField
import django.dispatch

from segno import helpers

# update_qr_code = django.dispatch.Signal()


#def get_next_card_id():
#    """
#    Returns the next card id for the current season. If there are no profiles, then the next card id is 1.
#    """
#    last = Registrations.objects.filter(season=Event.objects.get_active_season()).order_by('-cardID')[0:1]
#    if last:
#        return last.get().cardID + 1
#    else:
#        return 1

class RegistrationProfileManager(models.Manager):
    def get_registration_hackation(self, user, event_id):
        try:
            return Registrations.objects.get(user=user, event_id=event_id)
        except Registrations.DoesNotExist:
            return None

    def get_registrations(self, user):
        try:
            return Registrations.objects.get(user=user)
        except Registrations.DoesNotExist:
            return None

    def is_active(self, profile, active_season):
        if profile and active_season and str(profile.event) == str(active_season):
            return True
        else:
            return False


class Registrations(TimeStampMixin, models.Model):
    """This class adds a profile linked to a user who is registered"""

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, models.DO_NOTHING)
    #cardID = models.PositiveIntegerField(default=get_next_card_id)

    country = CountryField(blank=False, blank_label='(select country)')
    dietary_restrictions = models.TextField(max_length=250, default='', blank=True, null=True,
                                            verbose_name='Do you have any dietary restrictions?')
    phone_number = models.CharField(max_length=15, blank=False, null=False)

    # https://stackoverflow.com/questions/18108521/many-to-many-in-list-display-django
    ethnicity = models.ManyToManyField(EthnicityOption)
    is_minor = models.BooleanField(default=False, verbose_name='Under 18')

    # mlh_communication = models.BooleanField(default=False, verbose_name='MLH Communication')



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
    # TODO: MOVE THIS TO ENUM
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
        return "{}-{}".format(self.user.get_full_name(), self.user.email)

    def all_ethnicities(self):
        # return ",".join([e.value for e in obj.ethnicity.all()])
        return ', '.join(self.ethnicity.values_list('value', flat=True))
    def all_majors(self):
        # return ",".join([e.value for e in obj.ethnicity.all()])
        return ', '.join(self.major.values_list('value', flat=True))
    #def season_name(self):
    #    # return ",".join([e.value for e in obj.ethnicity.all()])
    #    return self.hackathon.season

    def get_qr_code(self):
        return helpers.make_vcard(name=self.user.full_name(),
                                  email=self.user.email,
                                  displayname=self.user.full_name()).svg_inline(scale=5, omitsize=True)

    #def mlh_data(self):
    #    return SocialAccount.objects.filter(user=self.user.id).first()

    #TODO: Added this to the form, but should copy it from the MLH data if it exists before presenting the form
    # def phone(self):
    #     data = self.mlh_data()
    #     if data is None:
    #         return 'No MLH Data'
    #     data = data.extra_data
    #     if 'phone_number' in data:
    #         return data['phone_number']
    #     return ''

    def age_by_competition(self):
        """
        Returns the age of the user at the time of the competition
        """
        return age_by_date(date_of_birth=str(self.user.date_of_birth), compare_date=self.event.start_date)

    # def clean(self):
    #     """
    #     Overrides the defualt clean function. Age has to be done in the form since user hasn't been linked yet
    #     """
    #     if self.is_coach and self.is_minor:
    #         raise ValidationError('Coaches cannot be minors')
    #     return super().clean()
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'event'], name='cnst_unique_userEvent'),
            #models.UniqueConstraint(fields=['event', 'cardID'], name='cnst_unique_eventCard'),
        ]


def age_by_date(date_of_birth: str, compare_date: datetime):
    """
    Returns the age of the user at the time of the competition
    """
    if date_of_birth == 'No MLH Data':
        return None
    birthday = datetime.strptime(date_of_birth, '%Y-%m-%d')
    # https://stackoverflow.com/questions/2217488/age-from-birthdate-in-python
    return compare_date.year - birthday.year - ((compare_date.month, compare_date.day) < (birthday.month, birthday.day))


@receiver(models.signals.post_delete, sender=Registrations)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.resume:
        if os.path.isfile(instance.resume.path):
            os.remove(instance.resume.path)


@receiver(models.signals.pre_save, sender=Registrations)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        userProfile = sender.objects.get(pk=instance.pk)
        old_file = userProfile.resume
    except sender.DoesNotExist:
        return False

    new_file = instance.resume
    if bool(old_file) and not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
