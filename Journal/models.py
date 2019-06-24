# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from PIL import Image


# Create your models here.
class Configurations(models.Model):
    conf_name = models.CharField(max_length=30)
    conf_val = models.CharField(max_length=30 , null=True , blank=True)
    pic_url = models.ImageField(upload_to='images' , null=True , blank=True)
    def __str__(self):
        return self.conf_name
    
class YearRange(models.Model):
    low_year = models.CharField(max_length=5)
    high_year = models.CharField(max_length=5)
    def __str__(self):
        return '%s - %s' % (self.low_year , self.high_year)
    
class Volumes(models.Model):
    volume_number = models.IntegerField(unique=True)
    yearrange = models.ForeignKey(YearRange , on_delete=models.CASCADE)
    def __str__(self):
        return "Volume %s" % (self.volume_number)

class Issues(models.Model):
    issue_number = models.IntegerField()
    month = models.CharField(max_length=15 , blank=True , null=True)
    year = models.CharField(max_length=5 , blank=True , null=True)
    pp = models.CharField(max_length=8 , null=True , blank=True)
    volume = models.ForeignKey(Volumes , on_delete=models.CASCADE)
    def __str__(self):
        return "Volume %s - Issue %s" % (self.volume.volume_number , self.issue_number)

class Article(models.Model):
    title = models.TextField()
    authors = models.CharField(max_length=400 , null=True , blank=True)
    pp = models.CharField(max_length=8 , null=True , blank=True)
    keywords = models.TextField(null=True , blank=True)
    abstract = models.TextField(null=True , blank=True)
    issue = models.ForeignKey(Issues , on_delete=models.CASCADE)
    cats = [('index' , 'index') , ('revs' , 'reviews') , ('RA' , 'research articles')]
    cat = models.CharField(max_length=6 , choices=cats , default='RA')
    refrences = models.TextField(null=True , blank=True)
    pdf = models.FileField(upload_to='pdfs')
    def __str__(self):
        return self.title

class users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    article = models.ForeignKey(Article , on_delete=models.CASCADE)
    def __str__(self):
        return self.username