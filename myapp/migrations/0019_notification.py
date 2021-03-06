# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 02:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_labprocedure_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=200)),
                ('ntype', models.CharField(max_length=50)),
                ('status', models.BooleanField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Profile')),
            ],
        ),
    ]
