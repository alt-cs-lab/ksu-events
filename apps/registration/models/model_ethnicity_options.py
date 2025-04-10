from django.db import models


class EthnicityOption(models.Model):
    key = models.CharField(max_length=4, blank=False, null=False)
    value = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.value