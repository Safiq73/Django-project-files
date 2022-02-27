
# Create your views here.
from operator import le
from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.
def index(request):
    blogs= BlogPost.objects.all()
    return render(request, 'blog/index.html', {'blogs':blogs})


def blogPost(request, id):
    previous=False
    next=False
    post=False
    lenth=len(BlogPost.objects.all())
    if id<=lenth and id>=1:
        post=BlogPost.objects.filter(post_id=id)[0]
    if id-1>=1:
        previous=BlogPost.objects.filter(post_id=id-1)[0]
    if id+1<=lenth:
        next=BlogPost.objects.filter(post_id=id+1)[0]
    return render(request, 'blog/blogPost.html', {"post":post, 'previous':previous, "next":next})