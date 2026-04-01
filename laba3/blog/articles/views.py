from django.shortcuts import render
from .models import Article  

def archive(request):
    """
    Отображает архив всех статей.
    """
    posts = Article.objects.all()  # Получаем все статьи из БД
    return render(request, 'articles/archive.html', {'posts': posts})