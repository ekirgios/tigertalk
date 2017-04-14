# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('blockedOrNot', models.BooleanField(default=False)),
                ('inappropriateCount', models.IntegerField(verbose_name='Inappropriate', default=0)),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('username', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField()),
                ('netid', models.CharField(max_length=50)),
                ('modOrNot', models.BooleanField(default=False)),
                ('blockedOrNot', models.BooleanField(default=False)),
                ('classYear', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='inappropriateId',
            field=models.ManyToManyField(related_name='+', to='tigertalk.User'),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(to='tigertalk.User'),
        ),
    ]
