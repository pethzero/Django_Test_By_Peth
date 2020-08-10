from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage


from .models import *
from .forms import *

def blog_list(request):
    data = Blog.objects.all()
    return render(request, 'blog_list.html',{'m':data})

def index(request):
    data = Blog.objects.all()
    return render(request, 'index.html',{'m':data})

def blog_detail(request, **kwargs):
    pk = kwargs['pk']
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})


def home(request):
    documents = Document.objects.all()
    return render(request, 'home.html', {'documents': documents})


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })
