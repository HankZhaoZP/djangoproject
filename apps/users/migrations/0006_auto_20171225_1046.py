# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-25 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20171225_1039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='birday',
            new_name='birthday',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
