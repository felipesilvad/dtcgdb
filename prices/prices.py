import requests
from cards.models import Card
import lxml
import gspread
import schedule
import time
import datetime
from bs4 import BeautifulSoup
from forex_python.converter import CurrencyRates

c = CurrencyRates()
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

cards = Card.objects.all().order_by('slug').first()

def request(URL_suruga_ya):
    URL_suruga_ya = URL_suruga_ya
    page_suruga_ya = requests.get(URL_suruga_ya, headers=headers)
    soup_suruga_ya = BeautifulSoup(page_suruga_ya.content, 'lxml')
    price_suruga_ya = soup_suruga_ya.find(class_="text-price-detail price-buy").text
    return price_suruga_ya

def parse(price_suruga_ya):
    jpy_suruga_ya = int(price_suruga_ya.replace('円 (税込)', ''))
    usd_suruga_ya = round((c.convert('JPY', 'USD', jpy_suruga_ya)), 2)
    date = datetime.datetime.today()
    values = {'card': 'BT1-000', 'date':date, 'jpy_suruga_ya': jpy_suruga_ya, 'usd_suruga_ya':usd_suruga_ya}
    return values

def output(values):
    gs = gspread.service_account(filename='prices\creds.json')
    sh = gs.open('DTCGprices').sheet1
    sh.update('A2', [[1, 2], [3, 4]])
    sh.append_row([values['card'], str(values['date']), values['jpy_suruga_ya'], values['usd_suruga_ya']])
    return

data = request('https://www.suruga-ya.jp/product/detail/GG646306')
values = parse(data)
output(values)