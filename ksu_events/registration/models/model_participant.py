from django.db import models

from ksu_events.events.models.mixins import TimeStampMixin
from ksu_events.registration.models.model_registrations import Registrations
from ksu_events.registration.formatChecker import ContentTypeRestrictedFileField
from ksu_events.registration.models.model_major_options import MajorOption


class Participant(TimeStampMixin, models.Model):

    registration = models.ForeignKey(Registrations, models.DO_NOTHING)
    qWhy = models.TextField(max_length=1000, default='',
                            verbose_name="Why do you want to participate in this event?")
    qExpectations = models.TextField(max_length=1000, default='',
                                     verbose_name='What do you hope to get out of this event?')
    qPrize = models.TextField(max_length=1000, default='',
                              verbose_name='Any cool prizes you would like to win? Share them here!', blank=True,
                              null=True)
    resume = ContentTypeRestrictedFileField(upload_to='resume/',
                                            content_types=['application/pdf'],
                                            max_upload_size=5242880, blank=True, null=True)
    major = models.ManyToManyField(MajorOption)

    # TODO: Also copy this from MLH?
    school = models.CharField(max_length=100, default='', blank=False, null=False)