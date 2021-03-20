from datetime import datetime
from prices import prices
from cards.models import Card

cards = Card.objects.all().order_by('number').filter(set__set_type="Booster")

def start():
    for i in range(1, len(cards)):
        data = prices.request(cards[i].suruga_ya)
        values = prices.parse(data)
        # prices.output(values, i)