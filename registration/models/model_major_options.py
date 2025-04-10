from django.db import models


class MajorOption(models.Model):
    key = models.CharField(max_length=4, blank=False, null=False)
    value = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.value