# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-11 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_remove_chlorosityfromrws_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='chlorosityfromrws',
            name='timestamp',
            field=models.IntegerField(default=1),
        ),
    ]
