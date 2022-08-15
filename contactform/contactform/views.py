
from django.core.files.storage import FileSystemStorage

from django.shortcuts import render
from contact.form import FormContactForm


def index(request):
    return render(request,'index.html')


def showform(request):
    form= FormContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form':form}
    return render(request,'contactform.html',context)


def fileupload(request):
    if request.method =='POST' and request.FILES['uploadefile']:
        getfile = request.FILES['uploadefile']
        fss =FileSystemStorage()
        filename = fss.save(getfile.name,getfile)
        uploaded_file_url =fss.url(filename)
        return render(request,'fileupload.html',{
            'uploaded_file_url':uploaded_file_url   
        })
    return render(request,'contactform.html')