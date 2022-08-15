
from audioop import reverse
from re import template
from unicodedata import name
from unittest import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from matplotlib.style import context
from sympy import arg
from cat.forms import MyForm

from cat.models import RedCat

# Create your views here.


def main(request):
    cat = RedCat.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'cat':cat,
    }
    return HttpResponse(template.render(context,request))
    
def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({},request))


def my_form(request):
    if request.method =="POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = MyForm()
        return render(request,'cv-form.html',{'form':form})