# Generated by Django 3.0.5 on 2020-04-14 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200414_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Provider',
            new_name='provider',
        ),
    ]
