# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-30 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyadar', '0016_studentscore'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentscore',
            name='max_score',
        ),
        migrations.AddField(
            model_name='class',
            name='max_score',
            field=models.IntegerField(default=100),
        ),
    ]
