from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index, name="blogHome"),
    path('blogPost/<int:id>', views.blogPost, name="blogPost"),

]
