from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_organisation = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
