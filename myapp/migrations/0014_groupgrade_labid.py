# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 10:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20171121_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupgrade',
            name='labid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.LabActivity'),
            preserve_default=False,
        ),
    ]
