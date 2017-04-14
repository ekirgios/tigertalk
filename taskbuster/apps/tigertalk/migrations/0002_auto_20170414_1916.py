# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tigertalk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('blockedOrNot', models.BooleanField(default=False)),
                ('inappropriateCount', models.IntegerField(verbose_name='Inappropriate', default=0)),
                ('helpfulCount', models.IntegerField(verbose_name='Helpful', default=0)),
                ('helpfulId', models.ManyToManyField(related_name='+', to='tigertalk.User')),
                ('inappropriateId', models.ManyToManyField(related_name='+', to='tigertalk.User')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
                'ordering': ('question', 'user'),
            },
        ),
        migrations.RenameField(
            model_name='question',
            old_name='date',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(to='tigertalk.Question'),
        ),
        migrations.AddField(
            model_name='answers',
            name='user',
            field=models.ForeignKey(to='tigertalk.User'),
        ),
    ]
