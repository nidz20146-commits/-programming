# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """
    Главная страница - возвращает ответ без явного указания content_type.
    """
    return HttpResponse('Привет, Мир!')

def home(request):
    return render(request, 'index.html', {})