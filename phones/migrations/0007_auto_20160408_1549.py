# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0006_auto_20160408_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extenddate',
            name='extend_branch',
            field=models.CharField(max_length=25, choices=[('Ahmet', 'Ahmet'), ('Aki', 'Aki'), ('Amersfoort', 'Amersfoort'), ('Antwerp', 'Antwerp'), ('Arap Breda', 'Arap Breda'), ('Atilla', 'Atilla'), ('Barca', 'Barca'), ('Birdman', 'Birdman'), ('BTC', 'BTC'), ('buuf', 'Buuf'), ('Denmark', 'Denmark'), ('Den Bosch', 'Den Bosch'), ('Deniz', 'Deniz'), ('Devrim', 'Devrim'), ('Eindhoven', 'Eindhoven'), ('Enschede', 'Enschede'), ('eniste', 'Eniste'), ('Europa', 'Europa'), ('grow', 'Grow'), ('hille', 'Hille'), ('Hilversum', 'Hilversum'), ('Homer', 'Homer'), ('Hoorn', 'Hoorn'), ('Ierland', 'Ierland'), ('Kenan', 'Kenan'), ('kinker', 'Kinker'), ('Kleine', 'Kleine'), ('mand', 'Mand'), ('Office', 'Office'), ('Omer Den', 'Omer Den'), ('Omer Rot', 'Omer Rot'), ('plein', 'Plein'), ('Prince', 'Prince'), ('Rado', 'Rado'), ('senti', 'Senti'), ('ser-ist', 'Sin-ist'), ('Spain', 'Spain'), ('st-weg', 'St-weg'), ('Sufi', 'Sufi'), ('Tarlock', 'Tarlock'), ('tol', 'Tol'), ('uzun', 'Uzun'), ('v.Wou', 'v.Wou'), ('viji', 'Viji'), ('Zub', 'Zub'), ('Zwager', 'Zwager'), ('Zwolle', 'Zwolle'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], blank=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='branch',
            field=models.CharField(max_length=15, choices=[('Ahmet', 'Ahmet'), ('Aki', 'Aki'), ('Amersfoort', 'Amersfoort'), ('Antwerp', 'Antwerp'), ('Arap Breda', 'Arap Breda'), ('Atilla', 'Atilla'), ('Barca', 'Barca'), ('Birdman', 'Birdman'), ('BTC', 'BTC'), ('buuf', 'Buuf'), ('Denmark', 'Denmark'), ('Den Bosch', 'Den Bosch'), ('Deniz', 'Deniz'), ('Devrim', 'Devrim'), ('Eindhoven', 'Eindhoven'), ('Enschede', 'Enschede'), ('eniste', 'Eniste'), ('Europa', 'Europa'), ('grow', 'Grow'), ('hille', 'Hille'), ('Hilversum', 'Hilversum'), ('Homer', 'Homer'), ('Hoorn', 'Hoorn'), ('Ierland', 'Ierland'), ('Kenan', 'Kenan'), ('kinker', 'Kinker'), ('Kleine', 'Kleine'), ('mand', 'Mand'), ('Office', 'Office'), ('Omer Den', 'Omer Den'), ('Omer Rot', 'Omer Rot'), ('plein', 'Plein'), ('Prince', 'Prince'), ('Rado', 'Rado'), ('senti', 'Senti'), ('ser-ist', 'Sin-ist'), ('Spain', 'Spain'), ('st-weg', 'St-weg'), ('Sufi', 'Sufi'), ('Tarlock', 'Tarlock'), ('tol', 'Tol'), ('uzun', 'Uzun'), ('v.Wou', 'v.Wou'), ('viji', 'Viji'), ('Zub', 'Zub'), ('Zwager', 'Zwager'), ('Zwolle', 'Zwolle'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], blank=True),
        ),
    ]
