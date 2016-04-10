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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Question', models.TextField(max_length=10000)),
                ('Answer', models.CharField(max_length=1000)),
                ('WaitTime', models.CharField(max_length=100)),
                ('WaitMessage', models.TextField(max_length=100000)),
                ('question_story', models.TextField(max_length=10000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Zealid', models.CharField(max_length=70)),
                ('CurrentQuestionNo', models.IntegerField(default=0)),
                ('LastSolvedAt', models.CharField(max_length=10000)),
                ('college', models.CharField(max_length=10000)),
                ('phno', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
