# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20150607_2103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['start_date', 'name']},
        ),
    ]
