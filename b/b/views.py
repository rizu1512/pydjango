


from re import template
from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')