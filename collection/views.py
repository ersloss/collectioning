from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from collection.forms import NewCollectionForm
from collection.models import Collection


def index(request):
    collections = Collection.objects.all().order_by('name')
    paginator = Paginator(collections, 25)
    page = request.GET.get('page')
    try:
        collections = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        collections = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        collections = paginator.page(paginator.num_pages)
    return render(request, 'collection/collection_index.html', {'collections': collections})


def add_collection(request):
    collection_form = NewCollectionForm(request.POST or None)
    return render(request, 'collection/add_collection.html', {'collection_form': collection_form})
