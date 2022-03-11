from http.client import HTTPResponse
import imp
from turtle import title
from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from blog.models import Blog

# Create your views here.

def home(request):
    return render(request, 'home/Home.html')
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        description=request.POST.get('description')
        if len(name)<3 or len(phone)<10 or len(description)<5:
            messages.error(request, 'Could not process the data, Make sure to enter the details correctly')
        else:
            contact=Contact(name=name, email=email, phone=phone, description=description)
            contact.save()
            messages.success(request, 'Successfully saved details, Will contact you soon..')
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def search(request):
    query=request.GET['query']
    # blog= Blog.objects.all()
    blog= Blog.objects.filter(title__icontains=query)
    params={"blog":blog} 
    return render(request, 'home/search.html', params)
