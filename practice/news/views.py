from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseNotFound, HttpResponseRedirect

from .models import News, Type


def index(request):
    template = 'news/index.html'
    news = News.objects.order_by('id').all()
    context = {
        'news': news,
    }
    return render(request, template, context)


def types(request, name):
    template = 'news/types_news.html'
    title = f'Новости типа - {name}'
    type = get_object_or_404(Type, name=name)
    news = News.objects.filter(type=type)
    context = {
        'title': title,
        'news': news,

    }
    return render(request, template, context)


def all_types(request):
    template = 'news/types_list.html'
    tips = Type.objects.order_by('id').all()
    context = {
        'tips': tips,
    }
    return render(request, template, context)


def delete_news(request, id):
    new = News.objects.get(id=id)
    new.delete()
    return HttpResponseRedirect("/")

def delete_type(request, id):
    typ = Type.objects.get(id=id)
    typ.delete()
    return HttpResponseRedirect("/")


def create_news(request):
    if request.method == "POST":
        news = News()
        news.name = request.POST.get("name")
        news.short_description = request.POST.get("short_description")
        news.full_description = request.POST.get("full_description")
        news.type = request.POST.get(Type.name)
        news.save()
    return HttpResponseRedirect("/")


def create_type(request):
    if request.method == "POST":
        type = Type()
        type.name = request.POST.get("name")
        type.color = request.POST.get("color")
        type.save()
    return HttpResponseRedirect("/")


def edit_news(request, id):
    template = 'news/edit_news.html'
    ex = '<h1>Новость не найдена</h1>'
    try:
        news = News.objects.get(id=id)
        context = {
            'news':news,
        }
        if request.method == "POST":
            news.name = request.POST.get("name")
            news.short_description = request.POST.get("short_description")
            news.full_description = request.POST.get("full_description")
            news.type = request.POST.get(Type.name)
            news.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, template, context)
    except News.DoesNotExist:
        return HttpResponseNotFound(ex)


def edit_type(request, id):
    template = 'news/edit_type.html'
    ex = '<h1>Тип не найден</h1>'
    try:
        type = Type.objects.get(id=id)
        context = {
            'type':type,

        }
        if request.method == "POST":
            type.name = request.POST.get("name")
            type.color = request.POST.get("color")
            type.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, template, context)
    except Type.DoesNotExist:
        return HttpResponseNotFound(ex)