"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from blog.views import post_list, post_detail, PostDetailView, PostListView, IndexView, TagView, CategoryView, SearchView, AuthorView
from config.views import links, LinkView
from comment.views import CommentView
from typeidea.custom_site import custom_site
from blog.rss import LatestPostFeed
from blog.apis import post_list, PostList, PostViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register(r'post', PostViewSet, base_name='api-post')
router.register(r'category', CategoryViewSet, base_name='api-category')

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='super-admin'),
    url(r'^super_admin/', custom_site.urls, name='admin'),

    # url(r'^$', post_list, name='index'),
    url(r'^$', IndexView.as_view(), name='index'),

    # url(r'^category/(?P<category_id>\d+)/$', post_list, name='category-list'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),

    # url(r'^tag/(?P<tag_id>\d+)/$', post_list, name='tag-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),

    # url(r'^post/(?P<post_id>\d+)/$', post_detail, name='post-detail'),
    url(r'^post/(?P<post_id>\d+)/$', PostDetailView.as_view(), name='post-detail'),



    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),

    # url(r'^links/$', links, name='links'),
    url(r'^links/$', LinkView.as_view(), name='links'),

    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^rss|feed/$', LatestPostFeed(), name='rss'),

    # url(r'^api/post/$', post_list, name='post-list'),
    # url(r'^api/post/$', LatestPostFeed(), name='rss'),
    url(r'^api/', include(router.urls)),

    url(r'^api/docs/', include_docs_urls(title='typeidea apis')),

]
