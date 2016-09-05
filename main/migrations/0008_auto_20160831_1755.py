# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-31 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160831_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='user_unique',
            field=models.CharField(default='unique', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='user_name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
    ]