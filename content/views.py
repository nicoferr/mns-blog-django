from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from datetime import datetime, timezone
from django.db.models import Q
from .forms import CommentForm
from django.contrib import messages

# Create your views here.
def articles_list(request):
    articles = Article.objects.all()
    # articles = Article.objects.filter(is_published=True, publication_date__lte=datetime.now(timezone.utc)).order_by('-publication_date')
    
    # articles = Article.objects.filter(title__iexact='mon premier article')
    # articles = Article.objects.filter(title__contains='article')
    # articles = Article.objects.filter(title__isnull=False)
    # articles = Article.objects.filter(title__in=['...','...'])
    # articles = Article.objects.filter(Q(author__isnull=False) | ~Q(title__icontains='premier')) #le ~ inverse la condition
    # articles = Article.objects.raw('SELECT * FROM content_article WHERE title=%s', ['Mon deuxième article'])
    
    return render(request,'list.html', {'articles': articles})

def articles_details(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                article=article,
                author=request.user if request.user.is_authenticated
                else None,
                content=form.cleaned_data['content']
            )
            comment.save()
            messages.success(request, 'Commentaire ajouté avec succès !')
            return redirect('articles_details', article_id=article_id)

    comments = article.comments.all().order_by('-created_at')
    return render(request, 'details.html', {'article':  article, 'comments': comments, 'form': form})