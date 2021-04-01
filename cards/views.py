from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Card, Set, Digimon, New
from .filters import CardFilter
from users.forms import Collection
from users.models import UserCard
from forex_python.converter import CurrencyRates
from datetime import datetime
from threading import Timer
import gspread

def setlist(request):
  page_title = 'Set List'
  sets = Set.objects.all().order_by('slug')
  return render(request, 'cards/setlist.html', {'page_title':page_title, 'sets': sets})

def card_detail(request, card_slug, slug_set):
  set = Set.objects.get(slug=slug_set)
  card = Card.objects.get(set=set, slug=card_slug)
  alternate_arts = card.alternate_art.order_by('number')
  alternate_art_c = alternate_arts.count()
  effect_main = card.effect.filter(effect_type="Main")
  effect_inheritable = card.effect.filter(effect_type="Inheritable")
  page_title = card.number
  previous_card = set.card_set.filter(slug__lt=card_slug).order_by('-slug')
  next_card = set.card_set.filter(slug__gt=card_slug).order_by('slug')

  gs = gspread.service_account(filename='creds.json')
  spreadsheet = gs.open('DTCGprices')
  sheet1 = spreadsheet.sheet1
  cell = sheet1.find(card.number)
  avg_usd = sheet1.cell(cell.row, 4).value
  yuyu_tei_jpy = sheet1.cell(cell.row, 5).value
  suruga_ya_jpy = sheet1.cell(cell.row, 7).value
  amazon_jp_jpy = sheet1.cell(cell.row, 9).value
  ebay_jp_jpy = sheet1.cell(cell.row, 11).value

  usercard=None
  usercard_sc = 0
  usercard_pc = 0
  if request.user.is_authenticated:
      usercard = UserCard.objects.all().filter(profile=request.user.profile).filter(card=card).first()
      # usercard_sc = usercard.annotate(total=Sum(F('quantity') + F('quantity_jp'))).filter(total__gt=0).count()
      # usercard_pc = usercard.annotate(total=Sum(F('quantity_parallel') + F('quantity_parallel_jp'))).filter(total__gt=0).count()
      if usercard != None:
          usercard_sc = usercard.quantity + usercard.quantity_jp
          usercard_pc = usercard.quantity_parallel + usercard.quantity_parallel_jp

  if request.method == 'POST':
    form = Collection(request.POST, instance=usercard)
    if form.is_valid():
      form.instance.profile = request.user.profile
      form.instance.card = card
      form.save()
      messages.success(request, 'Collection Updated')
      return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
  else:
    form = Collection()

  return render(request, 'cards/card_detail.html', {
    'page_title':page_title,'card':card, 'effect_main':effect_main, 'effect_inheritable':effect_inheritable,
    'previous_card':previous_card, 'next_card':next_card,
    'alternate_arts':alternate_arts, 'alternate_art_c':alternate_art_c,
    'avg_usd':avg_usd, 'yuyu_tei_jpy':yuyu_tei_jpy, 'suruga_ya_jpy':suruga_ya_jpy, 'amazon_jp_jpy':amazon_jp_jpy, 'ebay_jp_jpy':ebay_jp_jpy,
    'form': form, 'usercard':usercard , 'usercard_sc':usercard_sc, 'usercard_pc':usercard_pc
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
  # tParallel = set.card_set.filter(image_parallel_jp__icontains='.png').count()
  tParallel = 00

  return render(request, 'cards/set_detail.html', {'page_title':page_title, 'cards': cards, 'set': set,
  'tRed': tRed, 'tBlue':tBlue, 'tYellow':tYellow, 'tGreen':tGreen, 'tColorless':tColorless,
  'tC':tC, 'tU':tU,'tR':tR, 'tSR':tSR, 'tSEC':tSEC, 'tDigimon':tDigimon, 'tDigitama':tDigitama,
  'tTamer':tTamer, 'tOption':tOption, 'tParallel':tParallel  })

def search(request):
  page_title = 'Advanced Search'
  cards = Card.objects.all().order_by('card_type', 'lv', '-color', 'play_cost')
  sets = Set.objects.all().order_by('slug')
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
      Q(effect__effect_type__icontains=query)|
      Q(effect__effect_blue__icontains=query)|
      Q(effect__effect_purple__icontains=query)|
      Q(effect__effect_txt__icontains=query)|
      Q(effect__effect_txt_2__icontains=query)|
      Q(effect__effect_keyword__title__icontains=query)|
      Q(effect__effect_keyword__desc__icontains=query)|
      Q(promo_name__icontains=query)
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
  
  return render(request, 'cards/search.html', 
  {'page_title':page_title, 'cards': cards, 'myFilter': myFilter, 'page_obj': queryset, 'cards_count':cards_count,
  'sets':sets, 'digimons':digimons})

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
      # Q(effect_blue_1__icontains=query)|
      # Q(effect_purple_1__icontains=query)|
      # Q(effect_txt_1__icontains=query)|
      # Q(effect_keyword_1__icontains=query)|
      # Q(effect_blue_2__icontains=query)|
      # Q(effect_purple_2__icontains=query)|
      # Q(effect_txt_2__icontains=query)|
      # Q(effect_keyword_2__icontains=query)|
      # Q(effect_blue_3__icontains=query)|
      # Q(effect_purple_3__icontains=query)|
      # Q(effect_txt_3__icontains=query)|
      # Q(effect_keyword_3__icontains=query)|
      # Q(evolutionary_effect_blue_1__icontains=query)|
      # Q(evolutionary_effect_purple_1__icontains=query)|
      # Q(evolutionary_effect_txt_1__icontains=query)|
      # Q(evolutionary_effect_keyword_1__icontains=query)|
      # Q(evolutionary_effect_blue_2__icontains=query)|
      # Q(evolutionary_effect_purple_2__icontains=query)|
      # Q(evolutionary_effect_txt_2__icontains=query)|
      # Q(evolutionary_effect_keyword_2__icontains=query)|
      # Q(evolutionary_effect_blue_3__icontains=query)|
      # Q(evolutionary_effect_purple_3__icontains=query)|
      # Q(evolutionary_effect_txt_3__icontains=query)|
      # Q(evolutionary_effect_keyword_3__icontains=query)|
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

