from django.db import models
from django.utils.translation import gettext_lazy as _
from ubicacion.models import Barrio
from products.models import Product, ProductDetails


class Address(models.Model):
    barrio = models.ForeignKey(Barrio, on_delete=models.SET_NULL, null=True)
    address = models.CharField(_('address'), max_length=100)


class Branch(models.Model):
    name = models.CharField(max_length=15)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, blank=True, related_name='branch')
    products = models.ManyToManyField(Product, through=ProductDetails, verbose_name=_('product'))
    #service = models.ManyToManyField('Service', related_name='branches', verbose_name=_('service'))

