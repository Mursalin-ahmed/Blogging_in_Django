# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required  # This will ensure the user is logged in
from .models import Article
from .forms import ArticleForm

# List of all articles, only for logged-in users
@login_required
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})

# View an individual article
@login_required
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article_detail.html', {'article': article})

# Create a new article, only for logged-in users
@login_required
def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user  # Associate the article with the logged-in user
            article.save()
            return redirect('article-detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'blog/article_edit.html', {'form': form})

# Edit an existing article, only for logged-in users
@login_required
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article-detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/article_edit.html', {'form': form})

# Delete article view
@login_required
def article_confirm_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    

    if request.method == 'POST':
        article.delete()
        return redirect('article-list')  # Redirect to article list after deletion

    return render(request, 'blog/article_confirm_delete.html', {'article': article})
