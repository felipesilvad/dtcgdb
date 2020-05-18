from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Card, Set, Digimon, NewC
from .filters import CardFilter

def setlist(request):
    sets = Set.objects.all().order_by('release_date')
    return render(request, 'cards/setlist.html', {'sets': sets})

def card_detail(request, card_slug, slug_set):
    set = Set.objects.get(slug=slug_set)
    card = Card.objects.get(set=set, slug=card_slug)
    cards_in_set = set.card_set.all().order_by('slug')
    cards_in_set_reverse = set.card_set.all().order_by('-slug')
    return render(request, 'cards/card_detail.html', {'card':card, 'cards_in_set':cards_in_set,
    'card_slug':card_slug, 'cards_in_set_reverse':cards_in_set_reverse})

def set_detail(request, slug_set):
    set = Set.objects.get(slug=slug_set)
    cards = set.card_set.all().order_by('slug')
    tRed = set.card_set.filter(color='Red').count()
    tBlue = set.card_set.filter(color='Blue').count()
    tYellow = set.card_set.filter(color='Yellow').count()
    tGreen = set.card_set.filter(color='Green').count()
    tColorless = set.card_set.filter(color='Colorless').count()
    tC = set.card_set.filter(rarity='C').count()
    tU = set.card_set.filter(rarity='U').count()
    tR = set.card_set.filter(rarity='R').count()
    tSR = set.card_set.filter(rarity='SR').count()
    tSEC = set.card_set.filter(rarity='SEC').count()
    tDigimon = set.card_set.filter(card_type='Digimon').count()
    tDigitama = set.card_set.filter(card_type='Digitama').count()
    tTamer = set.card_set.filter(card_type='Tamer').count()
    tOption = set.card_set.filter(card_type='Option').count()

    return render(request, 'cards/set_detail.html', {'cards': cards, 'set': set,
    'tRed': tRed, 'tBlue':tBlue, 'tYellow':tYellow, 'tGreen':tGreen, 'tColorless':tColorless,
    'tC':tC, 'tU':tU,'tR':tR, 'tSR':tSR, 'tSEC':tSEC, 'tDigimon':tDigimon, 'tDigitama':tDigitama,
    'tTamer':tTamer, 'tOption':tOption })

def cardslist(request):
    cards = Card.objects.all().order_by('card_type', 'lv', '-color', 'play_cost')
    sets = Set.objects.all().order_by('-release_date')
    digimons = Digimon.objects.all().order_by('title')
    query = request.GET.get("q")
    if query:
        cards = cards.filter(
            Q(title__icontains=query)|
            Q(title_jp__icontains=query)|
            Q(artist__icontains=query)|
            Q(number__icontains=query)|
            Q(card_type__icontains=query)|
            Q(color__icontains=query)|
            Q(rarity__icontains=query)|
            Q(lv__icontains=query)|
            Q(dp__icontains=query)|
            Q(play_cost__icontains=query)|
            Q(evolution_cost_1__icontains=query)|
            Q(evolution_cost_1_color__icontains=query)|
            Q(evolution_cost_2__icontains=query)|
            Q(evolution_cost_2_color__icontains=query)|
            Q(effect_blue_1__icontains=query)|
            Q(effect_purple_1__icontains=query)|
            Q(effect_txt_1__icontains=query)|
            Q(effect_keyword_1__icontains=query)|
            Q(effect_blue_2__icontains=query)|
            Q(effect_purple_2__icontains=query)|
            Q(effect_txt_2__icontains=query)|
            Q(effect_keyword_2__icontains=query)|
            Q(effect_blue_3__icontains=query)|
            Q(effect_purple_3__icontains=query)|
            Q(effect_txt_3__icontains=query)|
            Q(effect_keyword_3__icontains=query)|
            Q(evolutionary_effect_blue_1__icontains=query)|
            Q(evolutionary_effect_purple_1__icontains=query)|
            Q(evolutionary_effect_txt_1__icontains=query)|
            Q(evolutionary_effect_keyword_1__icontains=query)|
            Q(evolutionary_effect_blue_2__icontains=query)|
            Q(evolutionary_effect_purple_2__icontains=query)|
            Q(evolutionary_effect_txt_2__icontains=query)|
            Q(evolutionary_effect_keyword_2__icontains=query)|
            Q(evolutionary_effect_blue_3__icontains=query)|
            Q(evolutionary_effect_purple_3__icontains=query)|
            Q(evolutionary_effect_txt_3__icontains=query)|
            Q(evolutionary_effect_keyword_3__icontains=query)|
            Q(promo_name__icontains=query)
        ).distinct()

    effect = request.GET.get("effect")
    if effect:
        cards = cards.filter(
            Q(effect_blue_1__icontains=effect)|
            Q(effect_purple_1__icontains=effect)|
            Q(effect_txt_1__icontains=effect)|
            Q(effect_keyword_1__icontains=effect)|
            Q(effect_blue_2__icontains=effect)|
            Q(effect_purple_2__icontains=effect)|
            Q(effect_txt_2__icontains=effect)|
            Q(effect_keyword_2__icontains=effect)|
            Q(effect_blue_3__icontains=effect)|
            Q(effect_purple_3__icontains=effect)|
            Q(effect_txt_3__icontains=effect)|
            Q(effect_keyword_3__icontains=effect)|
            Q(evolutionary_effect_blue_1__icontains=effect)|
            Q(evolutionary_effect_purple_1__icontains=effect)|
            Q(evolutionary_effect_txt_1__icontains=effect)|
            Q(evolutionary_effect_keyword_1__icontains=effect)|
            Q(evolutionary_effect_blue_2__icontains=effect)|
            Q(evolutionary_effect_purple_2__icontains=effect)|
            Q(evolutionary_effect_txt_2__icontains=effect)|
            Q(evolutionary_effect_keyword_2__icontains=effect)|
            Q(evolutionary_effect_blue_3__icontains=effect)|
            Q(evolutionary_effect_purple_3__icontains=effect)|
            Q(evolutionary_effect_txt_3__icontains=effect)|
            Q(evolutionary_effect_keyword_3__icontains=effect)
        ).distinct()

    effect_keyword = request.GET.get("effect_keyword")
    if effect_keyword:
        cards = cards.filter(
            Q(effect_keyword_1__icontains=effect_keyword)|
            Q(effect_keyword_2__icontains=effect_keyword)|
            Q(effect_keyword_3__icontains=effect_keyword)|
            Q(evolutionary_effect_keyword_1__icontains=effect_keyword)|
            Q(evolutionary_effect_keyword_2__icontains=effect_keyword)|
            Q(evolutionary_effect_keyword_3__icontains=effect_keyword)
        ).distinct()

        
    myFilter = CardFilter(request.GET, queryset=cards)
    cards = myFilter.qs

    paginator = Paginator(cards, 80)

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    cards_count = cards.count()
    
    return render(request, 'cards/cards_list.html', 
    {'cards': cards, 'myFilter': myFilter, 'page_obj': queryset, 'cards_count':cards_count,
    'sets':sets, 'digimons':digimons, 'effect':effect, 'effect_keyword':effect_keyword})