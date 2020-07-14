from django. shortcuts import render 
from django.http import HttpResponse
from .models import Blog

def blog_list(request):
    data = Blog.objects.all()
    return render(request, 'blog_list.html',{'m':data})

def blog_detail(request, **kwargs):
    pk = kwargs['pk']
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})