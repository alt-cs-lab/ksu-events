from datetime import datetime
from django.db import models

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,
                                      help_text='The time this record was created.')
    updated_at = models.DateTimeField(auto_now=True,
                                      help_text='The last time this record was updated.')

    class Meta:
        abstract = True
