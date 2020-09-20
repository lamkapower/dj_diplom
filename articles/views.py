from django.shortcuts import render

from articles.models import Article


def main_page(request):
    return render(
        request, 'pages/main.html', {'articles': Article.objects.all()})
