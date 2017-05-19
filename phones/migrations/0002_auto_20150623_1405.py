# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='key',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='pin',
            field=models.CharField(max_length=25, blank=True),
        ),
    ]
