from django.db import models


class Provider(models.Model):
    company = models.CharField(max_length=255)
    phone = models.BigIntegerField()
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    userProvider = models.CharField(max_length=255, blank=True)
    phoneProvider = models.BigIntegerField(blank=True)
    emailProvider = models.EmailField(max_length=255, blank=True)

    def __str__(self):
        return self.company
