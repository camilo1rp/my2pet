# Generated by Django 3.0.5 on 2020-04-16 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_auto_20200414_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='observationProduct',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
