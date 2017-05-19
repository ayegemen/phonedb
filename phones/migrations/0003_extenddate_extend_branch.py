# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_auto_20150623_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='extenddate',
            name='extend_branch',
            field=models.CharField(choices=[('Ahmet', 'Ahmet'), ('Amersfoort', 'Amersfoort'), ('Antwerp', 'Antwerp'), ('buuf', 'Buuf'), ('eniste', 'Eniste'), ('Europa', 'Europa'), ('grow', 'Grow'), ('hille', 'Hille'), ('Ierland', 'Ierland'), ('Kenan', 'Kenan'), ('kinker', 'Kinker'), ('mand', 'Mand'), ('Office', 'Office'), ('Omer Den', 'Omer Den'), ('Omer Rot', 'Omer Rot'), ('plein', 'Plein'), ('senti', 'Senti'), ('ser-ist', 'Sin-ist'), ('Spain', 'Spain'), ('st-weg', 'St-weg'), ('tol', 'Tol'), ('uzun', 'Uzun'), ('viji', 'Viji'), ('Zub', 'Zub')], max_length=25, blank=True),
        ),
    ]
