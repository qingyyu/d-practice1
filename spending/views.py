# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import User, BaseFile
# Create your views here.
def index(request):
    return HttpResponse("hello!")

def detail(request, basefile_id):
    
    return HttpResponse()

def basefile(request):
    bf = BaseFile.objects.all()
    context = {
        'basefiles': bf,
    }
    return HttpResponse(template.render(context,request))
