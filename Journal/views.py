# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def index(request):
    years = models.YearRange.objects.all().order_by('-low_year')
    for year in years:
        year.Volumes = year.volumes_set.all().order_by('-volume_number')
        for volume in year.Volumes:
            volume.issue = volume.issues_set.all().order_by('-issue_number')
    lastV = models.Volumes.objects.all().order_by('-volume_number')[:1]
    lastI = lastV[0].issues_set.all().order_by('-issue_number')[:1]
    context = {'years' : years , 'lasti' : lastI[0] , 'lastv' : lastV[0]} 
    return render(request , "Journal/index.html" , context)

def issues(request , vol , iss):
    lastV = models.Volumes.objects.all().order_by('-volume_number')[:1]
    lastI = lastV[0].issues_set.all().order_by('-issue_number')[:1]
    volume = models.Volumes.objects.get(volume_number=vol)
    issue = models.Issues.objects.get(issue_number=iss)
    articles = issue.article_set.all()
    for article in articles:
        if article.authors:
            article.authors = article.authors.split(",")
        if article.keywords:
            article.keywords = article.keywords.split(",")
    context = {'articles' : articles , 'issue' : issue , 'volume' : volume , 'vol' : vol , 'iss' : iss , 'lastv' : lastV[0] , 'lasti' : lastI[0]}
    return render(request , 'Journal/issue.html' , context)