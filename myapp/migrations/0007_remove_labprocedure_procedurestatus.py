# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-13 09:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20171113_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labprocedure',
            name='procedurestatus',
        ),
    ]
