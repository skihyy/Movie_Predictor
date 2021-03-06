# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('view', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AggregateInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_movies', models.IntegerField()),
                ('score', models.DecimalField(decimal_places=2, max_digits=20)),
                ('actor_score', models.DecimalField(decimal_places=2, max_digits=20)),
                ('actress_score', models.DecimalField(decimal_places=2, max_digits=20)),
                ('director_score', models.DecimalField(decimal_places=2, max_digits=20)),
                ('length_score', models.DecimalField(decimal_places=2, max_digits=20)),
                ('genre_score', models.DecimalField(decimal_places=2, max_digits=20)),
                ('avg_movie_box', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='movieinfo',
            old_name='actorIDs',
            new_name='actor_ids',
        ),
        migrations.RenameField(
            model_name='movieinfo',
            old_name='directorID',
            new_name='director_id',
        ),
        migrations.RemoveField(
            model_name='moviescore',
            name='actorScore',
        ),
        migrations.RemoveField(
            model_name='moviescore',
            name='directorScore',
        ),
        migrations.RemoveField(
            model_name='moviescore',
            name='genreScore',
        ),
        migrations.RemoveField(
            model_name='moviescore',
            name='lengthScore',
        ),
        migrations.AddField(
            model_name='moviescore',
            name='actor_score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviescore',
            name='actress_score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviescore',
            name='avg_movie_box',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviescore',
            name='director_score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviescore',
            name='genre_score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moviescore',
            name='length_score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='view.Genre'),
        ),
        migrations.AlterField(
            model_name='moviescore',
            name='score',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
