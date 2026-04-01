from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
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