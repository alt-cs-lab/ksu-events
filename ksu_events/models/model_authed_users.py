from django.db import models
from ksu_events.models.model_users import User

from ksu_events.models.mixins import TimeStampMixin

class Authed_Users(TimeStampMixin, models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    dateOfBirth = models.DateField()

    PARTICIPANT = "PAR"
    ORGAINIZER = "ORG"
    
    AUTH_LEVELS = {
        PARTICIPANT: "Participant",
        ORGAINIZER: "Orgainizer"
    }

    auth_level = models.CharField(max_length=2, choices=AUTH_LEVELS, blank=False)