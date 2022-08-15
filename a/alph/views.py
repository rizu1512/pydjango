from django.http import HttpResponse
from django.shortcuts import render
from requests import request

# Create your views here.
def index(request):
    return HttpResponse("hello")