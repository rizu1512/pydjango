from distutils.command.upload import upload
from fileinput import filename
from inspect import getfile
from django.shortcuts import render

from django.core.files.storage import FileSystemStorage

# Create your views here.


def fileupload(request):
    if request.method =='POST' and request.FILES['uploadefile']:
        getfile = request.FILES['uploadefile']
        fss =FileSystemStorage()
        filename = fss.save(getfile.name,getfile)
        uploaded_file_url =fss.url(filename)
        return render(request,'fileupload.html',{
            'uploaded_file_url':uploaded_file_url   
        })
    return render(request,'fileupload.html')