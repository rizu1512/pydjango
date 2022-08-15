from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    data= {
        'name':'Muhammad Rizwan',
        'age':21,
        'email':'rizwanbraq@gmail.com'
    }
    return render(request,'index.html',data)


def contact(request):
    return render(request,'contact.html')