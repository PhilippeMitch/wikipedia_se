from django.shortcuts import render
from .documents import WikiTitleDocument

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