# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-06 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='score_actor',
            field=models.FloatField(default=3, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='score_actress',
            field=models.FloatField(default=3, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='score_budget',
            field=models.FloatField(default=3, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='score_director',
            field=models.FloatField(default=3, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='score_investment',
            field=models.FloatField(default=3, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='score_movie_box',
            field=models.FloatField(default=3, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='score_prize',
            field=models.FloatField(default=3, max_length=3),
            preserve_default=False,
        ),
    ]
