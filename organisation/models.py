from django.db import models
from authentication.models import CustomUser
from sector.models import Sector


class Organisation(models.Model):
    organisation_name = models.CharField(max_length=255)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    object = models.Manager()

    def __str__(self):
        return self.organisation_name
