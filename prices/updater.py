from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from prices import prices

def start():
    data = prices.request('https://www.suruga-ya.jp/product/detail/GG646306')
    values = prices.parse(data)
    prices.output(values)