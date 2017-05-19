# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('email', models.EmailField(blank=True, verbose_name='email history', max_length=254)),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='email change date')),
            ],
        ),
        migrations.CreateModel(
            name='ExtendDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateField(blank=True, null=True, verbose_name='extend date')),
                ('extend_period', models.CharField(blank=True, choices=[('7', '1 week'), ('14', '2 weken'), ('21', '3 weken'), ('31', '1 maand'), ('91', '3 maanden'), ('180', '6 maanden')], max_length=15)),
                ('extend_enddate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('imei', models.CharField(blank=True, max_length=20)),
                ('pin', models.CharField(blank=True, max_length=15)),
                ('key', models.CharField(blank=True, max_length=15)),
                ('activation_date', models.DateField(blank=True, null=True)),
                ('activation_choice', models.CharField(blank=True, choices=[('90', '3 maanden'), ('182', '6 maanden'), ('365', '1 jaar')], max_length=15)),
                ('activation_enddate', models.DateField(blank=True, null=True)),
                ('phone_model', models.CharField(blank=True, choices=[('9320', '9320'), ('9720', '9720'), ('9900', '9900'), ('9790', '9790'), ('9360', '9360'), ('9105', '9105')], max_length=15)),
                ('sim', models.CharField(max_length=25)),
                ('secure_messaging', models.CharField(blank=True, max_length=25)),
                ('branch', models.CharField(blank=True, choices=[('Ahmet', 'Ahmet'), ('Amersfoort', 'Amersfoort'), ('Antwerp', 'Antwerp'), ('Buuf', 'Buuf'), ('Eniste', 'Eniste'), ('Europa', 'Europa'), ('Grow', 'Grow'), ('Hille', 'Hille'), ('Ierland', 'Ierland'), ('Kenan', 'Kenan'), ('Kinker', 'Kinker'), ('Mand', 'Mand'), ('Office', 'Office'), ('Omer Den', 'Omer Den'), ('Omer Rot', 'Omer Rot'), ('Plein', 'Plein'), ('Senti', 'Senti'), ('Sin-ist', 'Sin-ist'), ('Spain', 'Spain'), ('St-weg', 'St-weg'), ('Tol', 'Tol'), ('Uzun', 'Uzun'), ('Viji', 'Viji'), ('Zub', 'Zub')], max_length=15)),
                ('comment', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SimHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('sim', models.CharField(blank=True, verbose_name='sim history', max_length=25)),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='sim change date')),
                ('phone', models.ForeignKey(to='phones.Phone')),
            ],
        ),
        migrations.AddField(
            model_name='extenddate',
            name='phone',
            field=models.ForeignKey(to='phones.Phone'),
        ),
        migrations.AddField(
            model_name='emailhistory',
            name='phone',
            field=models.ForeignKey(to='phones.Phone'),
        ),
    ]
