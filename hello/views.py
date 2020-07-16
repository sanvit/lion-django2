from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
# Create your views here.

def home(req):
    blogs=Blog.objects
    return render(req,'home.html',{'blogobject':blogs,'title':'제목','header':'목록 보기','currentTab':1})

def new(req):
    return render(req,'new.html')

def create(req):
    if(req.method=='POST'):
        post=Blog()
        post.title=req.POST['title']
        post.body=req.POST['body']
        post.save()
    return redirect('home')

def update(req,post_id):
    onepost=get_object_or_404(Blog,pk=post_id)
    onepost.title = req.POST['title']
    onepost.body = req.POST['body']
    onepost.save()
    redirect(str(post_id))

def delete(req,post_id):
    onepost=get_object_or_404(Blog,pk=post_id)
    onepost.delete()
    redirect('home')
