# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 00:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_student_facultyid'),
    ]

    operations = [
        migrations.AddField(
            model_name='labprocedurestatus',
            name='labid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.LabActivity'),
            preserve_default=False,
        ),
    ]
