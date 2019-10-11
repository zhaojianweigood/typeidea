from django.shortcuts import render
from django.http import HttpResponse

from .models import Tag, Post


def post_list(request, category_id=None, tag_id=None):
    if tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            posts_list =[]
        else:
            posts_list = tag.post_set.filter(status=Post.STATUS_NORMAL)
    else:
        posts_list = Post.objects.filter(status=Post.STATUS_NORMAL)
        if category_id:
            posts_list = posts_list.filter(category_id=category_id)

    context = {
        'post_list': posts_list
    }
    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    context = {
        'post': post
    }
    return render(request, 'blog/detail.html', context=context)
