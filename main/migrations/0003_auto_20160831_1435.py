# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-31 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_aboutme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='answer_text',
            field=models.TextField(blank=True, default='', verbose_name='Текст ответа на отзыв'),
        ),
    ]