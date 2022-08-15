from re import template
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import BB
# Create your views here.

def index(request):
    myb_b=BB.objects.all().values()
    template = loader.get_template('b_b/index.html')
    context = {
        'myb_b':myb_b,
    }
    return HttpResponse(template.render(context,request))


def add(request):
    template = loader.get_template('b_b/add.html')
    return HttpResponse(template.render({},request))