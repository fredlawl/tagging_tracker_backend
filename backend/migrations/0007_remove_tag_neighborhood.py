# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-04 19:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20180111_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='neighborhood',
        ),
    ]
