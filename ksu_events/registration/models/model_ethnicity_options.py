#Django
from django.db import models

# This model is for the ethnicities in the registration page
class EthnicityOption(models.Model):
    value = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return  f"{self.value}"