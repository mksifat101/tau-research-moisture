from django.db import models
from authentication.models import User
from sector.models import Sector


class Organisation(models.Model):
    organisation_name = models.CharField(max_length=255)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)

    def __str__(self):
        return self.organisation_name
