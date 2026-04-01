from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Article

def archive(request):
    posts = Article.objects.all()
    return render(request, 'articles/archive.html', {'posts': posts})

def get_article(request, article_id):
    post = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/article.html', {'post': post})

def create_post(request):
    if not request.user.is_authenticated:
        raise Http404
    
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        text = request.POST.get("text", "").strip()
        
        if title and text:
            article = Article.objects.create(
                title=title,
                text=text,
                author=request.user
            )
            return redirect('get_article', article_id=article.id)
        else:
            form = {
                'title': title,
                'text': text,
                'errors': 'Не все поля заполнены'
            }
            return render(request, 'articles/create_post.html', {'form': form})
    
    return render(request, 'articles/create_post.html', {})

def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        password_confirm = request.POST.get("password_confirm", "").strip()
        
        if not username or not email or not password or not password_confirm:
            form = {
                'username': username,
                'email': email,
                'errors': 'Все поля обязательны для заполнения'
            }
            return render(request, 'articles/register.html', {'form': form})
        
        if password != password_confirm:
            form = {
                'username': username,
                'email': email,
                'errors': 'Пароли не совпадают'
            }
            return render(request, 'articles/register.html', {'form': form})
        
        try:
            User.objects.get(username=username)
            form = {
                'username': username,
                'email': email,
                'errors': 'Пользователь с таким именем уже существует'
            }
            return render(request, 'articles/register.html', {'form': form})
        except User.DoesNotExist:
            pass
        
        user = User.objects.create_user(username, email, password)
        login(request, user)
        return redirect('archive')
    
    return render(request, 'articles/register.html', {})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        
        if not username or not password:
            form = {
                'username': username,
                'errors': 'Заполните все поля'
            }
            return render(request, 'articles/login.html', {'form': form})
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('archive')
        else:
            form = {
                'username': username,
                'errors': 'Неверный логин или пароль'
            }
            return render(request, 'articles/login.html', {'form': form})
    
    return render(request, 'articles/login.html', {})

def user_logout(request):
    logout(request)
    return redirect('archive')