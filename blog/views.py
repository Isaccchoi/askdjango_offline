# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post
# Create your views here.

def post_list(request):
    qs = Post.objects.all()

    query = request.GET.get("query", "")
    if query:
        condition = Q(title__icontains=query) | Q(content__icontains=query)

        qs = qs.filter(condition)

    return render(request, 'blog/post_list.html', {"post_list": qs, "query": query,})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {"post": post})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)  #get_absolute_url로 이동
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        "form": form,
    })

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('blog:post_detail', post.id)

    else:
        form = PostForm(instance=post)

    return render(request, 'post_form.html', {'form': form,})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('blog:post_list')
    return render(request, 'blog/post_confirm_delete.html', {"post": post, })



# def mysum(request, x, y=0, z=0):
#     return HttpResponse(int(x) + int(y) + int(z))

# def mysum(request, numbers):
#     '''
#     result = 0
#     for number in numbers.split("/"):
#         result += int(number)
#         '''
#     result = sum(
#         int(number or 0)
#         for number in numbers.split('/')
#     )
#     return HttpResponse(result)