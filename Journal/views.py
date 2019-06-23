# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def index(request):
    years = models.YearRange.objects.all()
    context = {'years' : years} 
    return render(request , "Journal/index.html" , context)