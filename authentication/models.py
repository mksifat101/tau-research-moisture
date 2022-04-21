from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    user_type_data = ((1, "Admin"), (2, "Org"), (3, "Client"))
    user_type = models.CharField(
        default=2, choices=user_type_data, max_length=10)

# class User(AbstractUser):
#     firstname = models.CharField(max_length=255)
#     lastname = models.CharField(max_length=255)
#     is_organisation = models.BooleanField(default=False)
#     is_client = models.BooleanField(default=False)
