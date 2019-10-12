from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse

from blog.views import CommonViewMixin
from .models import Link


def links(request):
    return HttpResponse('links')


class LinkView(CommonViewMixin, ListView):
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    template_name = 'config/links.html'
    context_object_name = 'link_list'
