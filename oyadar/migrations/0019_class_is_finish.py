# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-06 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oyadar', '0018_studentscore_is_finish'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='is_finish',
            field=models.BooleanField(default=False),
        ),
    ]