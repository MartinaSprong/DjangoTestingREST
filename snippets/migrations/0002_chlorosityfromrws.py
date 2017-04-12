# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-10 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChlorosityFromRWS',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('categoryName', models.CharField(max_length=50)),
                ('parameterName', models.CharField(max_length=50)),
                ('value', models.IntegerField()),
                ('unit', models.CharField(max_length=50)),
                ('time', models.TimeField()),
                ('locationName', models.CharField(max_length=50)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
        ),
    ]