# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-24 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Journal', '0007_article_refrences'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pdf',
            field=models.FileField(default=1, upload_to='pdfs'),
            preserve_default=False,
        ),
    ]