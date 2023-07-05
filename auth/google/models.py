
from django.db import models

class UserData(models.Model):
    google_id = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
