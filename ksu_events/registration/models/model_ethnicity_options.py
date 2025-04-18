from django.db import models


class EthnicityOption(models.Model):
    value = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return  self.value