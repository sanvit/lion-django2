from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
# Create your views here.

def home(req):
    blogs=Blog.objects
    return render(req,'home.html',{'blogobject':blogs,'title':'목록 보기','header':'목록 보기','currentTab':1})

def new(req):
    return render(req,'new.html',{'title':'글쓰기','header':'새 글 쓰기','currentTab':2})

def create(req):
    if(req.method=='POST'):
        post=Blog()
        post.title=req.POST['title']
        post.body=req.POST['body']
        post.save()
    return redirect('/post/'+ str(post.id))

def post(request,post_id):
    onepost=get_object_or_404(Blog,pk=post_id)
    return render(request,'detail.html',{'onepost':onepost,'title':onepost.title, 'header':onepost.title, 'currentTab':3})

def update(req,post_id):
    onepost=get_object_or_404(Blog,pk=post_id)
    onepost.title = req.POST['title']
    onepost.body = req.POST['body']
    onepost.save()
    return redirect('/post/'+str(post_id))

def delete(req,post_id):
    onepost=get_object_or_404(Blog,pk=post_id)
    onepost.delete()
    return redirect('home')

def edit(req,post_id):
    onepost=get_object_or_404(Blog,pk=post_id)
    return render(req, 'update.html', {'onepost':onepost,'title':'수정 :: ' +str(onepost.title), 'header':'수정','currentTab':4})