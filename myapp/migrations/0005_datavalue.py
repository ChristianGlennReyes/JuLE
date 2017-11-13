# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-13 07:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20171113_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000)),
                ('groupid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.StudentGroup')),
                ('procedureid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.LabProcedure')),
            ],
        ),
    ]
