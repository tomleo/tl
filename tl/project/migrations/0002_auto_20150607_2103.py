# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(blank=True, to='project.Category'),
        ),
        migrations.AlterField(
            model_name='project',
            name='framework',
            field=models.ManyToManyField(blank=True, to='project.Framework'),
        ),
        migrations.AlterField(
            model_name='project',
            name='languages',
            field=models.ManyToManyField(blank=True, to='project.Lanuage'),
        ),
    ]
