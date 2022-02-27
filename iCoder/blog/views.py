from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog
# Create your views here.

def blogHome(request):
    blog=Blog.objects.all()
    print(blog)
    return render(request, 'blog/blogHome.html', {"blog":blog})

def blogPost(request, slug):
    post=Blog.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, 'blog/blogPost.html', context)

