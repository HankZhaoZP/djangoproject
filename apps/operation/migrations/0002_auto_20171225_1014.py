# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-25 02:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecomments',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2017, 12, 25, 10, 14, 3, 947004), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userask',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2017, 12, 25, 10, 14, 3, 947004), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2017, 12, 25, 10, 14, 3, 962629), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userfavorite',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2017, 12, 25, 10, 14, 3, 962629), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='add_time',
            field=models.DateField(default=datetime.datetime(2017, 12, 25, 10, 14, 3, 962629), verbose_name='发送时间'),
        ),
    ]
