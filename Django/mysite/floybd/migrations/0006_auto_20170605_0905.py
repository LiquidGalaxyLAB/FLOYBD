# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-05 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floybd', '0005_auto_20170605_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stop_times',
            name='arrival_time',
            field=models.TimeField(help_text='HH:MM:SS'),
        ),
        migrations.AlterField(
            model_name='stop_times',
            name='departure_time',
            field=models.TimeField(help_text='HH:MM:SS'),
        ),
    ]