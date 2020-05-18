import django_filters
from django.db.models import Q
from django_filters import RangeFilter, CharFilter, MultipleChoiceFilter, TypedChoiceFilter, BooleanFilter, OrderingFilter
from .models import Card

class CardFilter(django_filters.FilterSet):
    
    title = CharFilter(field_name='title', lookup_expr='icontains')
    number = CharFilter(field_name='number', lookup_expr='icontains')
    artist = CharFilter(field_name='artist', lookup_expr='icontains')
    dp = RangeFilter()
    lv = RangeFilter()
    play_cost = RangeFilter()

    o = OrderingFilter(
        fields=(
            ('title', 'title'),
            ('dp', 'dp'),
            ('lv', 'lv'),
            ('play_cost', 'play_cost'),
            ('card_type', 'card_type')
        ),
    )


    class Meta:
        model = Card
        fields = ['rarity', 'set', 'digimon', 'dp', 'lv', 'play_cost', 'card_type', 'color', 'artist', 'evolution_cost_1']
