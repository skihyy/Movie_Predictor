# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view', '0007_delete_preloadperson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aggregateinfo',
            name='actress_score',
        ),
        migrations.RemoveField(
            model_name='aggregateinfo',
            name='avg_movie_box',
        ),
        migrations.RemoveField(
            model_name='aggregateinfo',
            name='duration_score',
        ),
        migrations.RemoveField(
            model_name='movieinfo',
            name='actor_ids',
        ),
        migrations.RemoveField(
            model_name='movieinfo',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='moviescore',
            name='actor_score',
        ),
        migrations.RemoveField(
            model_name='moviescore',
            name='actress_score',
        ),
        migrations.RemoveField(
            model_name='moviescore',
            name='avg_movie_box',
        ),
        migrations.RemoveField(
            model_name='moviescore',
            name='duration_score',
        ),
        migrations.RemoveField(
            model_name='person',
            name='sex_is_male',
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='first_actor_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='second_actor_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviescore',
            name='actors_correlation_score',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviescore',
            name='director_genre_score',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviescore',
            name='first_actor_director_score',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviescore',
            name='first_actor_genre_score',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviescore',
            name='first_actor_score',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviescore',
            name='second_actor_director_score',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviescore',
            name='second_actor_genre_score',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviescore',
            name='second_actor_score',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aggregateinfo',
            name='actor_score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='aggregateinfo',
            name='director_score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='aggregateinfo',
            name='genre_score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='aggregateinfo',
            name='score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='moviescore',
            name='director_score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='moviescore',
            name='genre_score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='moviescore',
            name='score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='average_score',
            field=models.FloatField(),
        ),
    ]
