# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-20 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Journal', '0002_auto_20190620_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='pp',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
