# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-11 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0007_auto_20170411_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chlorosityfromrws',
            name='time',
            field=models.DateTimeField(default=1),
        ),
    ]
