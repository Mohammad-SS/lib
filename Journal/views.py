# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse , Http404 , HttpResponseRedirect
from . import models
import os
from django.conf import settings
from django.urls import reverse 
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

def articlesabs(request , pk):
    article = models.Article.objects.get(id=pk)
    lastV = models.Volumes.objects.all().order_by('-volume_number')[:1]
    lastI = lastV[0].issues_set.all().order_by('-issue_number')[:1]
    if article.authors:
            article.authors = article.authors.split(",")
    if article.keywords:
            article.keywords = article.keywords.split(",")
    context = {'article' : article , 'lastv' : lastV[0] , 'lasti' : lastI[0]}
    return render(request , 'Journal/abs.html' , context)
    # return HttpResponse("HELLO!")
    

def articlesref(request , pk):
    article = models.Article.objects.get(id=pk)
    lastV = models.Volumes.objects.all().order_by('-volume_number')[:1]
    lastI = lastV[0].issues_set.all().order_by('-issue_number')[:1]
    if article.authors:
        article.authors = article.authors.split(",")
    if article.keywords:
        article.keywords = article.keywords.split(",")
    if article.refrences:
        article.refrences = article.refrences.split("|")
    context = {'article' : article , 'lastv' : lastV[0] , 'lasti' : lastI[0]}
    return HttpResponse(article.refrences)
    # return render(request , 'Journal/refs.html' , context)
    

def articlespdf(request , pk):
    article = models.Article.objects.get(id=pk)
    lastV = models.Volumes.objects.all().order_by('-volume_number')[:1]
    lastI = lastV[0].issues_set.all().order_by('-issue_number')[:1]
    if article.authors:
            article.authors = article.authors.split(",")
    if article.keywords:
            article.keywords = article.keywords.split(",")
    context = {'article' : article , 'lastv' : lastV[0] , 'lasti' : lastI[0]}
    return render(request , 'Journal/pdfs.html' , context )    

def login(request , pk):
    if request.POST:
        username = request.POST['login']
        password = request.POST['password']
        user_exist = models.users.objects.filter(username = username).count()
        if user_exist :
            user = models.users.objects.get(username = username)
            ps = user.password
            if password == ps:
                if user.article.id == int(pk):
                    path = user.article.pdf.path
                    file_path = os.path.join(settings.MEDIA_ROOT, path)
                    if os.path.exists(file_path):
                        with open(file_path, 'rb') as fh:
                            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                            return response
                    raise Http404
                else:
                    err = "You have no Access to this Article"
            else:
                err = "Username Or Password is Wrong !"
        else :
            err ="Username Or Password is Wrong !"
    else:
        err = "Please enter Username and Password"
    request.session['error'] = err
    return HttpResponseRedirect(reverse('articlepdf' , kwargs={'pk': pk}))


