# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-24 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_groupgrade_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='labprocedure',
            name='item',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
