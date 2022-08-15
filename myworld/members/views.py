from re import X, template
from tkinter import Y
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from sympy import content, false
from .models import Members 
from django.urls import reverse
# Create your views here.
def index(request):
    mymember = Members.objects.all().values()
    template =loader.get_template('index.html')
    context = {
        'mymembers' : mymember,
    }
    return HttpResponse(template.render(context,request))



def add(request):
    return render(request,'add.html')


def addrecord(request):
    x=request.POST.get('first',False)
    y=request.POST['last']
    member =Members(firstname=x,lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))       



def delete(request,id):
    member =Members.objects.get(id=id)
    member.delete()
    return render(request,'index')


def update(request, id):
    mymember = Members.objects.get(id=id)
    template =loader.get_template('update.html')
    content ={
        'mymember':mymember,
    }
    return HttpResponse(template.render(context,request))



def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))