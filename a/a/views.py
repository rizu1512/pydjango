

from django.http import HttpResponse
from django.shortcuts import render
from requests import request


def index(request):
    return HttpResponse("heelo")