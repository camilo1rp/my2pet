from django.contrib.auth.models import User
from django.db import models


class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30)
    dob = models.DateField()
    gender = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    race = models.CharField(max_length=30)
    comments = models.CharField(max_length=200)
    vaccines = models.CharField(max_length=200)
