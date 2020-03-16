import random
from django.db import models
from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=3)
    reference = models.CharField(max_length=15, null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='branch')
    available = models.BooleanField(default=False)
    delivery = models.BooleanField(default=False)
    #image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    discount = models.IntegerField()
    description = models.TextField(max_length=500, null=True, blank=True)
    #quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def codi(self):
        letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
        valor = random.sample(letras, 1) + random.sample('0123456789', 2)
        codigo = ''.join(map(str, valor))
        return codigo

    def save(self, *args, **kwargs):
        if not self.code:
            code_gen = self.codi()
            while code_gen in [pro.code for pro in Product.objects.all()]:
                code_gen = self.codi()
            self.code = code_gen
        if self.quantity < 1:
            self.available = False
        super(Product, self).save(*args, **kwargs)

