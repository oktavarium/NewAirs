# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-31 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_story'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_name', models.CharField(max_length=100, verbose_name='Название новости')),
                ('news_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата новости')),
                ('news_text', models.TextField(default='', verbose_name='Текст новости')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.AlterModelOptions(
            name='story',
            options={'verbose_name': 'События из жизни', 'verbose_name_plural': 'События из жизни'},
        ),
    ]
