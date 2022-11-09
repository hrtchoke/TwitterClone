
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else: 
            return HttpResponseRedirect(form.errors.as_json())


    posts = Post.objects.all()[:20]
    return render (request, 'posts.html',
                 {'posts':posts})
    

def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')


def edit(request,post_id):
    post=Post.objects.get(id=post_id)
    if request.method =='GET':
        return render(request, 'edit.html',{ 'post':post})

    if request.method =="POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
     

def likes(request, post_id):
            newlikecount = Post.objects.get(id=post_id)
            newlikecount.likecount += 1
            liked = True
            newlikecount.save()
            return HttpResponseRedirect('/')
