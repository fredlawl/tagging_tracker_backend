# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-13 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_address_type_of_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='date_taken',
            field=models.DateField(default='2013-12-17'),
            preserve_default=False,
        ),
    ]
