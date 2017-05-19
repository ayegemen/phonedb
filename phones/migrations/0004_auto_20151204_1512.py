# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_extenddate_extend_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extenddate',
            name='extend_branch',
            field=models.CharField(choices=[('Ahmet', 'Ahmet'), ('Aki', 'Aki'), ('Amersfoort', 'Amersfoort'), ('Antwerp', 'Antwerp'), ('Arap Breda', 'Arap Breda'), ('Atilla', 'Atilla'), ('Barca', 'Barca'), ('Birdman', 'Birdman'), ('buuf', 'Buuf'), ('Deniz', 'Deniz'), ('Eindhoven', 'Eindhoven'), ('eniste', 'Eniste'), ('Europa', 'Europa'), ('grow', 'Grow'), ('hille', 'Hille'), ('Hoorn', 'Hoorn'), ('Ierland', 'Ierland'), ('Kenan', 'Kenan'), ('kinker', 'Kinker'), ('Kleine', 'Kleine'), ('mand', 'Mand'), ('Office', 'Office'), ('Omer Den', 'Omer Den'), ('Omer Rot', 'Omer Rot'), ('plein', 'Plein'), ('Prince', 'Prince'), ('Rado', 'Rado'), ('senti', 'Senti'), ('ser-ist', 'Sin-ist'), ('Spain', 'Spain'), ('st-weg', 'St-weg'), ('Tarlock', 'Tarlock'), ('tol', 'Tol'), ('uzun', 'Uzun'), ('viji', 'Viji'), ('Zub', 'Zub'), ('Zwager', 'Zwager')], max_length=25, blank=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='branch',
            field=models.CharField(choices=[('Ahmet', 'Ahmet'), ('Aki', 'Aki'), ('Amersfoort', 'Amersfoort'), ('Antwerp', 'Antwerp'), ('Arap Breda', 'Arap Breda'), ('Atilla', 'Atilla'), ('Barca', 'Barca'), ('Birdman', 'Birdman'), ('buuf', 'Buuf'), ('Deniz', 'Deniz'), ('Eindhoven', 'Eindhoven'), ('eniste', 'Eniste'), ('Europa', 'Europa'), ('grow', 'Grow'), ('hille', 'Hille'), ('Hoorn', 'Hoorn'), ('Ierland', 'Ierland'), ('Kenan', 'Kenan'), ('kinker', 'Kinker'), ('Kleine', 'Kleine'), ('mand', 'Mand'), ('Office', 'Office'), ('Omer Den', 'Omer Den'), ('Omer Rot', 'Omer Rot'), ('plein', 'Plein'), ('Prince', 'Prince'), ('Rado', 'Rado'), ('senti', 'Senti'), ('ser-ist', 'Sin-ist'), ('Spain', 'Spain'), ('st-weg', 'St-weg'), ('Tarlock', 'Tarlock'), ('tol', 'Tol'), ('uzun', 'Uzun'), ('viji', 'Viji'), ('Zub', 'Zub'), ('Zwager', 'Zwager')], max_length=15, blank=True),
        ),
    ]
