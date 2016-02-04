# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20150607_2237'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lanuage',
            new_name='Language',
        ),
    ]
