# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-20 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190420_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='last_updated_time',
            field=models.DateField(auto_now=True),
        ),
    ]