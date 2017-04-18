# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tigertalk', '0003_auto_20170414_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ('text',),
            },
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(related_name='answers', to='tigertalk.Question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(related_name='answers', to='tigertalk.User'),
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(related_name='questions', to='tigertalk.User'),
        ),
        migrations.AddField(
            model_name='tag',
            name='questions',
            field=models.ManyToManyField(related_name='tags', to='tigertalk.Question'),
        ),
    ]
