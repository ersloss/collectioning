from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from models import Card


def index(request):
    cards_list = Card.objects.all().order_by('name')
    query = request.GET.get('query')

    if query is not None:
        cards_list = Card.objects.filter(name__icontains=query).order_by('name')

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


def card_details(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'cards/card_details.html', {'card': card})
