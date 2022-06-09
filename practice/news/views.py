from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Main page')

def types(request, slug):
    return HttpResponse(f'Type - {slug}')
