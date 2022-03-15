from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Blog, BlogComment
from django.contrib import messages

# Create your views here.

def blogHome(request):
    blog=Blog.objects.all()
    return render(request, 'blog/blogHome.html', {"blog":blog})

def blogPost(request, slug):
    post=Blog.objects.filter(slug=slug).first()
    com=BlogComment.objects.filter(post=post, parent=None)
    replies=BlogComment.objects.filter(post=post).exclude(parent=None)
    
    replyDict={}
    for i in replies:
        if i.parent.sNo not in replyDict.keys():
            replyDict[i.parent.sNo]=[i]
        else:
            replyDict[i.parent.sNo].append(i)
    print(replyDict)
    context={"post":post , "comments":com, "replyDict":replyDict}
    return render(request, 'blog/blogPost.html', context)

def postComment(request):
    if request.method=="POST":
        comment=request.POST['comment']
        postId=request.POST['post']
        parentComment=request.POST['parentComment']
        post=Blog.objects.filter(blogId=postId).first()
        user=request.user  
        if parentComment=='':                  
            comment=BlogComment(comment=comment, post=post, user=user)
            comment.save()        
            messages.success(request, 'Comment posted successfully')
        else:
            parent= BlogComment.objects.get(sNo=parentComment)
            comment=BlogComment(comment=comment, post=post, user=user, parent=parent)
            comment.save()        
            messages.success(request, 'Reply posted successfully')
        return redirect(f'/blog/{post.slug}')