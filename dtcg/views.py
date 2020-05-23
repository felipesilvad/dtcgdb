from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cards.models import Card, Set, Digimon, New

def home(request):
    page_title = 'Home'
    news = New.objects.all().order_by('-id')[:4:1]
    new_cards = Card.objects.all().order_by('-new_date')[:12:1]
    random_cards = Card.objects.all().order_by('?')[:12:1]
    return render(request, 'home.html', {'page_title':page_title, 'new_cards': new_cards,
     'random_cards': random_cards, 'news':news})

def card_images(request):
    page_title = 'Card Images'
    return render(request, 'card_images.html', {'page_title':page_title})

def new_detail(request, id=id):
    new = New.objects.get(id=id)
    page_title = new.title
    return render(request, 'cards/new_detail.html', {'new': new, 'page_title':page_title})

def news(request):
    page_title = 'News'
    news = New.objects.all().order_by('-id')

    paginator = Paginator(news, 80)

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    return render(request, 'cards/news.html', {'page_title':page_title, 'news': news, 'page_obj': queryset})