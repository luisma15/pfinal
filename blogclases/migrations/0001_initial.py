# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('al_nombre', models.CharField(max_length=20)),
                ('al_apellido', models.CharField(max_length=20)),
                ('al_edad', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('as_fecha', models.DateField()),
                ('as_aula', models.CharField(max_length=5)),
                ('as_alumno', models.ForeignKey(to='blogclases.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Catedratico',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('cat_nombre', models.CharField(max_length=20)),
                ('cat_apellido', models.CharField(max_length=20)),
                ('cat_genero', models.CharField(max_length=9)),
                ('cat_edad', models.CharField(max_length=2)),
                ('cat_telefono', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('cur_nombre', models.CharField(max_length=15)),
                ('cur_creditos', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='asignacion',
            name='as_catedratico',
            field=models.ForeignKey(to='blogclases.Catedratico'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='as_curso',
            field=models.ForeignKey(to='blogclases.Curso'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='al_asignaciones',
            field=models.ManyToManyField(to='blogclases.Curso', through='blogclases.Asignacion'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='al_catedratico',
            field=models.ManyToManyField(to='blogclases.Catedratico', through='blogclases.Asignacion'),
        ),
    ]
