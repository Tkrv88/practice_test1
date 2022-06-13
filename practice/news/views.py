from multiprocessing import context
from django.shortcuts import get_object_or_404, render

from .models import News, Type


def index(request):
    template = 'news/index.html'
    news = News.objects.all()
    context = {
        'news': news,
    }
    return render(request, template, context)


def types(request, name):
    template = 'news/types_news.html'
    title = f'Новости типа - {name}'
    # group = get_object_or_404(Group, slug=slug)
    # posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    type = get_object_or_404(Type, name=name)
    news = News.objects.filter(type=type)
    context = {
        'title': title,
        'news': news,

    }
    return render(request, template, context)


def all_types(request):
    template = 'news/types_list.html'
    tips = Type.objects.all()
    context = {
        'tips': tips,
    }
    return render(request, template, context)