


import email
from email.policy import default
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')


def about(request):
    mail= request.GET.get('Email',default)
    password=request.GET.get('Password')
    data = {'Email':email
           , 'password':password }
    return render(request,'about.html',data)


def contact(request):
    return render(request,'contact.html')
