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
    context = {'years' : years} 
    return render(request , "Journal/index.html" , context)