# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-25 02:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citydict',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2017, 12, 25, 10, 14, 3, 962629)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2017, 12, 25, 10, 14, 3, 962629)),
        ),
    ]
