from django.http import HttpResponse
from django.shortcuts import render
from cards.models import Card, Set, Digimon, NewC

def home(request):
    page_title = 'Home'
    new_cards = NewC.objects.all().order_by('-id')[:12:1]
    random_cards = Card.objects.all().order_by('?')[:12:1]
    return render(request, 'home.html', {'page_title':page_title, 'new_cards': new_cards, 'random_cards': random_cards})