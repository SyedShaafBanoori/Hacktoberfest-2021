# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-01 03:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0014_auto_20180531_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discussion',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='quizorassignment',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='discussion',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='classroom.Discussion'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
