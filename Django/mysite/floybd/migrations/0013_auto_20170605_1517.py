# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-05 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floybd', '0012_auto_20170605_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='agency_name',
            field=models.CharField(max_length=200),
        ),
    ]
