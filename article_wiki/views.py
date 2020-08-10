from django.shortcuts import render
from titre_wiki.models import TitreWiki
from .tasks import UpdateArticle
# Create your views here.


def add_article(request):
    UpdateArticle.start_job()
    return render(request, 'fill/article.html') 



