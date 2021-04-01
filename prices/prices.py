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

cards = Card.objects.all().order_by('number').filter(set__set_type="Booster")

def request(URL_suruga_ya):
  if URL_suruga_ya == None:
    price_suruga_ya = None
  else:
    try:
      page_suruga_ya = requests.get(URL_suruga_ya, headers=headers)
      soup_suruga_ya = BeautifulSoup(page_suruga_ya.content, 'lxml')
      price_suruga_ya = soup_suruga_ya.find(class_="text-price-detail price-buy").text
    except:
      price_suruga_ya = None
  return price_suruga_ya

def parse(price_suruga_ya):
  if price_suruga_ya == None:
    date = datetime.datetime.today()
    jpy_suruga_ya = None
    usd_suruga_ya = None
    values = {'date':date, 'jpy_suruga_ya': jpy_suruga_ya, 'usd_suruga_ya':usd_suruga_ya}
  else:
    jpy_suruga_ya = int(price_suruga_ya.replace('円 (税込)', ''))
    usd_suruga_ya = round((c.convert('JPY', 'USD', jpy_suruga_ya)), 2)
    date = datetime.datetime.today()
    values = {'date':date, 'jpy_suruga_ya': jpy_suruga_ya, 'usd_suruga_ya':usd_suruga_ya}
  return values

def output(values, i):
  gs = gspread.service_account(filename='prices\creds.json')
  spreadsheet = gs.open('DTCGprices')
  sheet1 = spreadsheet.sheet1
  valo = []

  valo.append([cards[i].number, cards[i].title])
  rng = "'" + sheet1._properties['title'] + "'!B2"
  rng = "Sheet1!A%s"(i)
  spreadsheet.values_update(rng, params={'valueInputOption': 'USER_ENTERED'}, body={'values': valo})


  # sheet1.update('A2', [[cards[i].number, cards[i].title, str(values['date']), values['jpy_suruga_ya'], values['usd_suruga_ya']]])
  # sheet1.update_cell(i, 1, cards[i].number)
  # sheet1.update_cell(i, 2, cards[i].title)
  # sheet1.update_cell(i, 3, str(values['date']))
  # if values['jpy_suruga_ya'] == None:
  #     sheet1.update_cell(i, 4, "-")
  # else:
  #     sheet1.update_cell(i, 4, values['jpy_suruga_ya'])
  return
