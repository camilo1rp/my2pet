# Generated by Django 3.0.3 on 2020-02-21 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20200220_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='company'),
        ),
    ]
