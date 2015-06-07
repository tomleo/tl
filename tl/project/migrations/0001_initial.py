# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('about', models.TextField()),
            ],
            options={
                'abstract': False,
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('about', models.TextField()),
            ],
            options={
                'abstract': False,
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Lanuage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('about', models.TextField()),
            ],
            options={
                'abstract': False,
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('categories', models.ManyToManyField(blank=True, null=True, to='project.Category')),
                ('framework', models.ManyToManyField(blank=True, null=True, to='project.Framework')),
                ('languages', models.ManyToManyField(blank=True, null=True, to='project.Lanuage')),
            ],
        ),
    ]
