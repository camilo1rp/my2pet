# Generated by Django 3.0.5 on 2020-04-16 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0003_provider_observationproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='provider',
            old_name='observationProduct',
            new_name='observations',
        ),
    ]
