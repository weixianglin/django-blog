# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-31 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170529_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='en_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='英文标题'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.CharField(default='/static/img/article/default.jpg', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='is_top',
            field=models.BooleanField(default=False, verbose_name='置顶'),
        ),
    ]
