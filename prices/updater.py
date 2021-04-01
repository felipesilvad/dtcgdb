# from datetime import datetime
# from apscheduler.schedulers.background import BackgroundScheduler
# from prices import prices
# from cards.models import Card

# cards = Card.objects.all().order_by('number').filter(set__set_type="Booster")
# # cards[i].suruga_ya
# def start():
#     for i in range(1, len(cards)):
#       data = prices.request('https://www.suruga-ya.jp/product/detail/GG738019')
#       values = prices.parse(data)
#       prices.output(values, i)