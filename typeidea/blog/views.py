from django.shortcuts import render
from django.http import HttpResponse

from .models import Tag, Post, Category


def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None
    if tag_id:
        posts_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        posts_list, category = Post.get_by_category(category_id)
    else:
        posts_list = Post.latest_posts()

    context = {
        'post_list': posts_list,
        'tag': tag,
        'category': category,
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
