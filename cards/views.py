from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Card, Set, Digimon, New
from .filters import CardFilter
import lxml
import requests
from bs4 import BeautifulSoup
from forex_python.converter import CurrencyRates


def setlist(request):
    page_title = 'Set List'
    sets = Set.objects.all().order_by('release_date')
    return render(request, 'cards/setlist.html', {'page_title':page_title, 'sets': sets})

def card_detail(request, card_slug, slug_set):
    set = Set.objects.get(slug=slug_set)
    card = Card.objects.get(set=set, slug=card_slug)
    page_title = card.number
    previous_card = set.card_set.filter(slug__lt=card_slug).order_by('-slug')
    next_card = set.card_set.filter(slug__gt=card_slug).order_by('slug')

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    c = CurrencyRates()

    jpy_yuyu_tei = None
    usd_yuyu_tei = None
    if card.yuyu_tei:
        URL_yuyu_tei = card.yuyu_tei
        page_yuyu_tei = requests.get(URL_yuyu_tei, headers=headers)
        soup_yuyu_tei = BeautifulSoup(page_yuyu_tei.content, 'lxml')
        price_yuyu_tei = soup_yuyu_tei.find(class_="price").b.text
        jpy_yuyu_tei = int(price_yuyu_tei.replace('円', ''))
        usd_yuyu_tei = round((c.convert('JPY', 'USD', jpy_yuyu_tei)), 2)


    jpy_suruga_ya = None
    usd_suruga_ya = None
    if card.suruga_ya:
        URL_suruga_ya = card.suruga_ya
        page_suruga_ya = requests.get(URL_suruga_ya, headers=headers)
        soup_suruga_ya = BeautifulSoup(page_suruga_ya.content, 'lxml')
        price_suruga_ya = soup_suruga_ya.find(class_="text-red text-bold mgnL10").text
        jpy_suruga_ya = int(price_suruga_ya.replace('円 (税込)', ''))
        usd_suruga_ya = round((c.convert('JPY', 'USD', jpy_suruga_ya)), 2)


    jpy_amazon_jp = None
    usd_amazon_jp = None
    if card.amazon_jp:
        URL_amazon_jp = card.amazon_jp
        page_amazon_jp = requests.get(URL_amazon_jp, headers=headers)
        soup_amazon_jp = BeautifulSoup(page_amazon_jp.content, 'lxml')
        price_amazon_jp = soup_amazon_jp.find(id="priceblock_ourprice")
        if price_amazon_jp:
            price_amazon_jp = soup_amazon_jp.find(id="priceblock_ourprice").text
            jpy_amazon_jp = int(price_amazon_jp.replace('￥', '').replace('¥', '').replace(',', ''))
            usd_amazon_jp = round((c.convert('JPY', 'USD', jpy_amazon_jp)), 2)


    usd_price_ebay = None
    jpy_price_ebay = None
    if card.ebay:
        URL_ebay = card.ebay
        page_ebay = requests.get(URL_ebay, headers=headers)
        soup_ebay = BeautifulSoup(page_ebay.content, 'lxml')
        price_ebay = soup_ebay.find(id="prcIsum").get('content')
        usd_price_ebay = float(price_ebay)
        jpy_price_ebay = round((c.convert('USD', 'JPY', usd_price_ebay)))

    usd = [usd_yuyu_tei, usd_suruga_ya, usd_amazon_jp, usd_price_ebay]
    usd_res = [] 
    for val in usd: 
        if val != None : 
            usd_res.append(val)
    
    usd_average = None
    if usd_res != []:
        usd_average = round(sum(usd_res) / len(usd_res), 2)

    return render(request, 'cards/card_detail.html', {
        'page_title':page_title,'card':card,'previous_card':previous_card, 'next_card':next_card,
        'jpy_yuyu_tei':jpy_yuyu_tei, 'jpy_suruga_ya':jpy_suruga_ya, 'jpy_amazon_jp':jpy_amazon_jp, 'usd_price_ebay':usd_price_ebay,
        'usd_yuyu_tei':usd_yuyu_tei, 'usd_suruga_ya':usd_suruga_ya, 'usd_amazon_jp':usd_amazon_jp, 'jpy_price_ebay':jpy_price_ebay,
        'usd_average':usd_average
    })


def set_detail(request, slug_set):
    set = Set.objects.get(slug=slug_set)
    page_title = set.title
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

    return render(request, 'cards/set_detail.html', {'page_title':page_title, 'cards': cards, 'set': set,
    'tRed': tRed, 'tBlue':tBlue, 'tYellow':tYellow, 'tGreen':tGreen, 'tColorless':tColorless,
    'tC':tC, 'tU':tU,'tR':tR, 'tSR':tSR, 'tSEC':tSEC, 'tDigimon':tDigimon, 'tDigitama':tDigitama,
    'tTamer':tTamer, 'tOption':tOption })

def cardslist(request):
    page_title = 'Advanced Search'
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
    {'page_title':page_title, 'cards': cards, 'myFilter': myFilter, 'page_obj': queryset, 'cards_count':cards_count,
    'sets':sets, 'digimons':digimons, 'effect':effect, 'effect_keyword':effect_keyword})

