from django.db import models

from categories.models import Category
from providers.models import Provider
from my2pet.helpers import code


class Product(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=3, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    reference = models.CharField(max_length=15, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True, related_name='products')
    # image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.code:
            code_gen = code()
            while code_gen in [pro.code for pro in Product.objects.all()]:
                code_gen = code()
            self.code = code_gen
        # if self.quantity < 1:
        #     self.available = False
        super(Product, self).save(*args, **kwargs)


class ProductDetails(models.Model):
    branch = models.ForeignKey(to='branches.Branch', on_delete=models.CASCADE, default=None)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    available = models.BooleanField(default=False)
    delivery = models.BooleanField(default=False)
    discount = models.CharField(max_length=50)
    quantity = models.IntegerField()
    observations = models.CharField(max_length=255, blank=True)