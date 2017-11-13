# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 10:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('facultyid', models.IntegerField(primary_key=True, serialize=False)),
                ('facultyname', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('gradeid', models.FloatField(primary_key=True, serialize=False)),
                ('grademin', models.IntegerField(blank=True, null=True)),
                ('grademax', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='GroupGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gradeid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Grade')),
            ],
        ),
        migrations.CreateModel(
            name='LabActivity',
            fields=[
                ('labid', models.IntegerField(primary_key=True, serialize=False)),
                ('labname', models.CharField(max_length=100, unique=True)),
                ('labsummary', models.TextField(blank=True, null=True)),
                ('hidden', models.IntegerField()),
                ('selected', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LabProcedure',
            fields=[
                ('procedureid', models.IntegerField(primary_key=True, serialize=False)),
                ('stepnum', models.IntegerField()),
                ('proceduredesc', models.TextField()),
                ('procedurestatus', models.IntegerField()),
                ('minvalue', models.IntegerField(blank=True, null=True)),
                ('maxvalue', models.IntegerField(blank=True, null=True)),
                ('labid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.LabActivity')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userType', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sensors',
            fields=[
                ('sensorid', models.IntegerField(primary_key=True, serialize=False)),
                ('sensorname', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentid', models.IntegerField(primary_key=True, serialize=False)),
                ('studentname', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('groupid', models.IntegerField(primary_key=True, serialize=False)),
                ('groupname', models.CharField(blank=True, max_length=45, null=True)),
                ('facultyid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Faculty')),
            ],
        ),
        migrations.AddField(
            model_name='labprocedure',
            name='sensorid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Sensors'),
        ),
        migrations.AddField(
            model_name='groupgrade',
            name='groupid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.StudentGroup'),
        ),
        migrations.AddField(
            model_name='groupgrade',
            name='procedureid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.LabProcedure'),
        ),
        migrations.AddField(
            model_name='group',
            name='groupid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.StudentGroup'),
        ),
        migrations.AddField(
            model_name='group',
            name='studentid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Student'),
        ),
    ]