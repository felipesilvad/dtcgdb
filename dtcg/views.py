from django.http import HttpResponse
from django.shortcuts import render
from cards.models import Card, Set, Digimon, NewC

def home(request):
    new_cards = NewC.objects.all().order_by('-id')[:12:1]
    random_cards =Card.objects.all().order_by('?')[:12:1]
    return render(request, 'home.html', {'new_cards': new_cards, 'random_cards': random_cards})