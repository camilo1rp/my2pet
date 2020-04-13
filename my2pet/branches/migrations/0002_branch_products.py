# Generated by Django 3.0.5 on 2020-04-07 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200407_2218'),
        ('branches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='products',
            field=models.ManyToManyField(through='products.ProductDetails', to='products.Product', verbose_name='product'),
        ),
    ]