from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article, Images


def Home(request):
    """
    View for the homepage.

    Retrieves all articles from the database and orders them by date.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered response containing the 'practice/base.html' template and 'articles' data.
    """
    articles = Article.objects.all().order_by('date')
    return render(request, 'practice/base.html', {'articles': articles})


@login_required(login_url="/accounts/login/")
def article_detail(request, slug):
    """
    View for displaying article details, requiring login.

    Retrieves the article with the given 'slug' from the database and retrieves all associated images.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the article.

    Returns:
        HttpResponse: Rendered response containing the 'practice/article-detail.html' template,
            'article', and 'images' data.
    """
    article = Article.objects.get(slug=slug)
    images = Images.objects.filter(article=article)
    return render(request, 'practice/article-detail.html', {'article': article, 'images': images})
