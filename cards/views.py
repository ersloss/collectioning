from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from models import Card


def index(request):
    cards_list = Card.objects.all().order_by('name')
    paginator = Paginator(cards_list, 25)
    page = request.GET.get('page')
    try:
        cards = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        cards = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        cards = paginator.page(paginator.num_pages)
    return render(request, 'cards/cards_index.html', {'cards': cards})
