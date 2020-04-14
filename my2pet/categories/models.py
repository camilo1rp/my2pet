import random
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=5)

    def __str__(self):
        """String representation"""
        return self.name

    def codi(self):
        letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
        valor = random.sample(letras, 2) + random.sample('0123456789', 3)
        codigo = ''.join(map(str, valor))
        return codigo

    def save(self, *args, **kwargs):
        if not self.code:
            code_gen = self.codi()
            while code_gen in [cat.code for cat in Category.objects.all()]:
                code_gen = self.codi()
            self.code = code_gen
        super(Category, self).save(*args, **kwargs)