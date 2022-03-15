from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
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
    if len(query)>100:
        blog=[]     
    else:
        blogTitle= Blog.objects.filter(title__icontains=query)
        blogAuthor= Blog.objects.filter(content__icontains=query)
        blogContent= Blog.objects.filter(title__icontains=query)
        blog=blogTitle.union(blogAuthor, blogContent)
    params={"blog":blog} 
    if len(blog)==0:
        messages.warning(request, 'No results')
    return render(request, 'home/search.html', params)

def handleSignup(request):
    if request.method=='POST':
        userName=request.POST['Username']
        fName=request.POST['fname']
        lName=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
               
        # checks
        if pass1 !=pass2:
            messages.error(request, "Password fields must be same")
            return redirect('home')
        
        # creating the user
        myUser=User.objects.create_user(userName, email, pass1)
        myUser.first_name=fName
        myUser.last_name=lName
        myUser.save()
        messages.success(request, "Your account has been created")
        return redirect('home')
    else:
        return HttpResponse('404- Operation failed')
    
    
def handleLogin(request):
    if request.method=='POST':
        userName=request.POST['Username']
        password=request.POST['pass']
        
        user=authenticate(request, username=userName, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")   
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")   
            return redirect('home')
    else:
        messages.error(request, "Invalid credentials")   
        return redirect('home')
        
    
def handleLogout(request):
    logout(request)
    return redirect('home')