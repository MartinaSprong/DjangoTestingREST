# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-11 14:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0009_chlorosity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChlorosityFromRWS',
        ),
    ]
