from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.db.models import Q

from config.models import SideBar
from .models import Tag, Post, Category


class PostListView(DetailView):
    queryset = Post.latest_posts()
    paginate_by = 1
    context_object_name = 'post_list'
    template_name = 'blog/list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'


class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super(CommonViewMixin, self).get_context_data(**kwargs)
        context.update({
            'sidebars': SideBar.get_all(),
        })
        context.update(Category.get_navs())
        return context


class IndexView(CommonViewMixin, ListView):
    queryset = Post.latest_posts()
    paginate_by = 2
    context_object_name = 'post_list'
    template_name = 'blog/list.html'


class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category': category
        })
        return context

    def get_queryset(self):
        queryset = super(CategoryView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)


class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag,
        })
        return context

    def get_queryset(self):
        """根据需求过滤"""
        queryset = super(TagView, self).get_queryset()
        tag_id = self.kwargs.get('tag_id')
        print(tag_id, '1113123')
        return queryset.filter(tag__id=tag_id)


class SearchView(IndexView):
    def get_context_data(self):
        context = super(SearchView, self).get_context_data()
        context.update({
            'keyword': self.request.GET.get('keyword', '')
        })
        return context

    def get_queryset(self):
        queryset = super(SearchView, self).get_queryset()
        keyword = self.request.GET.get('keyword')
        print(keyword)
        if not keyword:
            return queryset
        return queryset.filter(Q(title_icontains=keyword)| Q(desc__icontains=keyword))


class AuthorView(IndexView):
    def get_queryset(self):
        query_set = super(AuthorView, self).get_queryset()
        author_id = self.kwargs.get('owner_id')
        return query_set.filter(owner_id=author_id)


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
        'sidebars': SideBar.get_all(),
    }
    context.update(Category.get_navs())
    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    context = {
        'post': post,
        'sidebars': SideBar.get_all(),
    }
    context.update(Category.get_navs())
    return render(request, 'blog/detail.html', context=context)
