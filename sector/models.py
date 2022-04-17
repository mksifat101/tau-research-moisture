from django.db import models


class Sector(models.Model):
    sector_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.sector_name
