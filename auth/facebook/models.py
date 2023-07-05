
from django.db import models

class FBUserData(models.Model):
    facebook_id = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
