from django. shortcuts import render 
from django.http import HttpResponse
from .models import Blog

def index(request):
    #tags=['Red','Blue']
    #rock = 4
    data = Blog.objects.all()
    return render(request, 'index.html',{'m':data})

