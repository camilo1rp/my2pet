import random
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from branches.models import Branch
from categories.models import Category


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(_('code'), max_length=5, null=True, blank=True)
    company = models.CharField(_('company'), max_length=30, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='categories',
                                 verbose_name=_('category'))
    branch = models.ManyToManyField(Branch, related_name='company', verbose_name=_('branch'))

    def codi(self):
        letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
        valor = random.sample(letras, 2) + random.sample('0123456789', 3)
        codigo = ''.join(map(str, valor))
        return codigo

    def save(self, *args, **kwargs):
        if not self.code:
            code_gen = self.codi()
            while code_gen in [prof.code for prof in Profile.objects.all()]:
                code_gen = self.codi()
            self.code = code_gen
        super(Profile, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance).save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.CharField(max_length=20, default='', blank=True)
    address = models.CharField( max_length=100, default='', blank=True)
    id_type = models.CharField( max_length=100, default='', blank=True)
    id_number = models.IntegerField(blank=True)
    phone = models.BigIntegerField(blank=True)
    is_client = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_user_client(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance).save()

@receiver(post_save, sender=User)
def save_user_client(sender, instance, **kwargs):
    instance.client.save()
