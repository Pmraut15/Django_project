from django import template
from django.shortcuts import redirect, render

# Create your views here.
from django.template import loader
from django.http import HttpResponse
from django.http import request

from .models import newmodel

def indexrequest(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def pagesubmit(request):
    nm=request.POST.get('name')
    anonm=request.POST.get('anothername')

    submit=newmodel(name=nm,another_name=anonm)
    submit.save()
    
    