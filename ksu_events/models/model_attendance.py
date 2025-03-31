from django.db import models
import json

from ksu_events.models import Event, User
from ksu_events.models.mixins import TimeStampMixin
#from ksu_events.registration.models.model_registration import Registrations

class EventAttendance(TimeStampMixin, models.Model):

    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    #registeration_order = models.DateTimeField(auto_now_add=True)
    ethnicity = models.CharField(max_length=500, default='')
    country = models.CharField(max_length=500, default='')
    is_minor = models.BooleanField(default=False, verbose_name='Under 18')
    
    EDUCATION_LEVEL_CHOICES = [
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
    education_level= models.CharField(max_length=4, blank=False, null=False,
                                      choices=EDUCATION_LEVEL_CHOICES,
                                      verbose_name="Education Level")

    PARTICIPATION_CHOICES = [
        ('N/A', 'Not Sure'),
        ('ONL', 'Online'),
        ('INP', 'In-person'),
    ]
    participation_medium = models.CharField(max_length=4, blank=False, null=False,
                                     choices=PARTICIPATION_CHOICES,
                                     default='INP',
                                     verbose_name="How do you plan to participate in Hack K-State?")

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
    
    dietary_restrictions = models.TextField(max_length=250, default='', blank=True, null=True,
                                            verbose_name='Do you have any dietary restrictions?')
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'hackathon'], name='cnst_unique_userHackathon'),
            models.UniqueConstraint(fields=['hackathon', 'cardID'], name='cnst_unique_hackathonCard'),
        ]

    def __str__(self):
        return f"{self.user.full_name()} registered for {self.event.name}"

    
    #registration = models.ForeignKey(Registrations, blank=False, null=False, on_delete=models.CASCADE)

    #class Meta:
        #unique_together = (("registration", "created_at"),)

    #def toObj(self):
        #return {'id': self.pk, 'eventID': self.registration.event.pk, 'user': self.registration.user.pk, 'created_at': str(self.created_at),
            #'updated_at': str(self.updated_at)}
    
    #@staticmethod
    #def attendance_count(registration, event):
        #return EventAttendance.objects.filter(registration=registration, eventID=event).count()
    