# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Configurations(models.Model):
    conf_name = models.CharField(max_length=30)
    conf_val = models.CharField(max_length=30)
    pic_url = models.ImageField(upload_to='images')

class YearRange(models.Model):
    low_year = models.CharField(max_length=5)
    high_year = models.CharField(max_length=5)

class Volumes(models.Model):
    volume_number = models.IntegerField(unique=True)
    yearrange = models.ForeignKey(YearRange , on_delete=models.CASCADE)

class Issues(models.Model):
    issue_number = models.IntegerField()
    month = models.CharField(max_length=15)
    year = models.CharField(max_length=5)
    pp = models.CharField(max_length=8)
    volume = models.ForeignKey(Volumes , on_delete=models.CASCADE)

class Article(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=100)
    pp = models.CharField(max_length=8)
    keywords = models.TextField()
    abstract = models.TextField()
    issue = models.ForeignKey(Issues , on_delete=models.CASCADE)

class users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    article = models.ForeignKey(Article , on_delete=models.CASCADE)