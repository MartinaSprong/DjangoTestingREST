# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-11 13:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20170411_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chlorosityfromrws',
            name='time',
        ),
    ]