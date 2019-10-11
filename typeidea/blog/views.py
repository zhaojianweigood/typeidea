from django.shortcuts import render
from django.http import HttpResponse


def post_list(request, category_id=None, tag_id=None):

    context = {
        'name': 'post_list'
    }
    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id):
    context = {
        'name': 'post_detail'
    }
    return render(request, 'blog/detail.html', context=context)
