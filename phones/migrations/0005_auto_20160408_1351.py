# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0004_auto_20151204_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extenddate',
            name='extend_branch',
            field=models.CharField(blank=True, choices=[('Ahmet', 'Ahmet'), ('Aki', 'Aki'), ('Amersfoort', 'Amersfoort'), ('Antwerp', 'Antwerp'), ('Arap Breda', 'Arap Breda'), ('Atilla', 'Atilla'), ('Barca', 'Barca'), ('Birdman', 'Birdman'), ('BTC', 'BTC'), ('buuf', 'Buuf'), ('Denmark', 'Denmark'), ('Den Bosch', 'Den Bosch'), ('Deniz', 'Deniz'), ('Eindhoven', 'Eindhoven'), ('Enschede', 'Enschede'), ('eniste', 'Eniste'), ('Europa', 'Europa'), ('grow', 'Grow'), ('hille', 'Hille'), ('Hilversum', 'Hilversum'), ('Homer', 'Homer'), ('Hoorn', 'Hoorn'), ('Ierland', 'Ierland'), ('Kenan', 'Kenan'), ('kinker', 'Kinker'), ('Kleine', 'Kleine'), ('mand', 'Mand'), ('Office', 'Office'), ('Omer Den', 'Omer Den'), ('Omer Rot', 'Omer Rot'), ('plein', 'Plein'), ('Prince', 'Prince'), ('Rado', 'Rado'), ('senti', 'Senti'), ('ser-ist', 'Sin-ist'), ('Spain', 'Spain'), ('st-weg', 'St-weg'), ('Sufi', 'Sufi'), ('Tarlock', 'Tarlock'), ('tol', 'Tol'), ('uzun', 'Uzun'), ('v.Wou', 'v.Wou'), ('viji', 'Viji'), ('Zub', 'Zub'), ('Zwager', 'Zwager'), ('Zwolle', 'Zwolle')], max_length=25),
        ),
        migrations.AlterField(
            model_name='extenddate',
            name='extend_period',
            field=models.CharField(blank=True, choices=[('91', '3 maanden'), ('180', '6 maanden')], max_length=15),
        ),
        migrations.AlterField(
            model_name='phone',
            name='activation_choice',
            field=models.CharField(blank=True, choices=[('90', '3 maanden'), ('182', '6 maanden')], max_length=15),
        ),
        migrations.AlterField(
            model_name='phone',
            name='branch',
            field=models.CharField(blank=True, choices=[('Ahmet', 'Ahmet'), ('Aki', 'Aki'), ('Amersfoort', 'Amersfoort'), ('Antwerp', 'Antwerp'), ('Arap Breda', 'Arap Breda'), ('Atilla', 'Atilla'), ('Barca', 'Barca'), ('Birdman', 'Birdman'), ('BTC', 'BTC'), ('buuf', 'Buuf'), ('Denmark', 'Denmark'), ('Den Bosch', 'Den Bosch'), ('Deniz', 'Deniz'), ('Eindhoven', 'Eindhoven'), ('Enschede', 'Enschede'), ('eniste', 'Eniste'), ('Europa', 'Europa'), ('grow', 'Grow'), ('hille', 'Hille'), ('Hilversum', 'Hilversum'), ('Homer', 'Homer'), ('Hoorn', 'Hoorn'), ('Ierland', 'Ierland'), ('Kenan', 'Kenan'), ('kinker', 'Kinker'), ('Kleine', 'Kleine'), ('mand', 'Mand'), ('Office', 'Office'), ('Omer Den', 'Omer Den'), ('Omer Rot', 'Omer Rot'), ('plein', 'Plein'), ('Prince', 'Prince'), ('Rado', 'Rado'), ('senti', 'Senti'), ('ser-ist', 'Sin-ist'), ('Spain', 'Spain'), ('st-weg', 'St-weg'), ('Sufi', 'Sufi'), ('Tarlock', 'Tarlock'), ('tol', 'Tol'), ('uzun', 'Uzun'), ('v.Wou', 'v.Wou'), ('viji', 'Viji'), ('Zub', 'Zub'), ('Zwager', 'Zwager'), ('Zwolle', 'Zwolle')], max_length=15),
        ),
    ]
