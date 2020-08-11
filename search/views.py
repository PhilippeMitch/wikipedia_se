from django.shortcuts import render
from background_task.models import Task, CompletedTask
from django.utils import timezone

from .documents import WikiTitleDocument
from titre_wiki.models import TitreWiki



# Create your views here.
def search(request):
    q = request.GET.get('q')
    if q:
        titre_wiki = WikiTitleDocument.search().query('match', title=q)
        print('Search found')
    else:
        titre_wiki = ''
        print('serach not found')

    return render(request, 'search/search.html', {'titre_wiki': titre_wiki} )

def home(request):
    liste_titre = TitreWiki.objects.all()
    context = {'liste_titre': liste_titre}
    return render(request, 'home/home.html', context)







