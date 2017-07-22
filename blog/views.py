# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    qs = Post.objects.all()

    query = request.GET.get("query", "")
    if query:
        condition = Q(title__icontains=query) |
        Q(content__icontains=query)

        qs = qs.filter(condition)

    return render(request, 'blog/post_list.html', {"post_list": qs, "query": query,})

# def mysum(request, x, y=0, z=0):
#     return HttpResponse(int(x) + int(y) + int(z))

def mysum(request, numbers):
    '''
    result = 0
    for number in numbers.split("/"):
        result += int(number)
        '''
    result = sum(
        int(number or 0)
        for number in numbers.split('/')
    )
    return HttpResponse(result)
