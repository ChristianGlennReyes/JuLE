# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20171121_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupgrade',
            name='gradeid',
        ),
        migrations.AddField(
            model_name='groupgrade',
            name='grade',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='labactivity',
            name='maximumpoint',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
