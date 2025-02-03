from django.db import models

from ksu_events.models.mixins import TimeStampMixin
from ksu_events.models.model_authed_users import Authed_Users
from ksu_events.models.model_events import Event

class Orgainizers(TimeStampMixin, models.Model):
    user = models.ForeignKey(Authed_Users, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
