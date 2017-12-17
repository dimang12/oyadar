# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-06 21:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oyadar', '0020_class_professor_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_class', models.IntegerField()),
                ('attended', models.IntegerField()),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oyadar.Class')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
