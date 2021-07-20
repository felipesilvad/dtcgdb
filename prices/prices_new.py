import requests
import lxml
import gspread
import schedule
import time
import datetime
from bs4 import BeautifulSoup
from forex_python.converter import CurrencyRates

c = CurrencyRates()
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

gs = gspread.service_account(filename='prices/creds.json')
spreadsheet = gs.open('DTCGprices')
bt = spreadsheet.sheet1

def yuyu_tei(range):
  for i in range:
    time.sleep(3)
    URL_yuyu_tei = bt.cell(i, 37).value
    print(bt.cell(i, 1).value)
    if URL_yuyu_tei:
      page_yuyu_tei = requests.get(URL_yuyu_tei, headers=headers)
      soup_yuyu_tei = BeautifulSoup(page_yuyu_tei.content, 'lxml')
      price_yuyu_tei = soup_yuyu_tei.find(class_="price").b.text
      jpy_yuyu_tei = int(price_yuyu_tei.replace('円', ''))
      usd_yuyu_tei = round((c.convert('JPY', 'USD', jpy_yuyu_tei)), 2)
      if jpy_yuyu_tei != bt.cell(i, 5).value:
        bt.update_cell(i, 5, jpy_yuyu_tei)
      if jpy_yuyu_tei != bt.cell(i, 6).value:
        bt.update_cell(i, 6, usd_yuyu_tei)
    else:
      if bt.cell(i, 5).value != "-":
        bt.update_cell(i, 5, "-")
      if bt.cell(i, 6).value != "-":
        bt.update_cell(i, 6, "-")

def suruga_ya(range):
  for i in range:
    time.sleep(3)
    URL_suruga_ya = bt.cell(i, 38).value
    print(bt.cell(i, 1).value)
    if URL_suruga_ya:
      page_suruga_ya = requests.get(URL_suruga_ya, headers=headers)
      soup_suruga_ya = BeautifulSoup(page_suruga_ya.content, 'lxml')
      try:
        price_suruga_ya = soup_suruga_ya.find(class_="text-price-detail price-buy").text
        jpy_suruga_ya = int(price_suruga_ya.replace('円 (税込)', '').replace(',', ''))
        usd_suruga_ya = round((c.convert('JPY', 'USD', jpy_suruga_ya)), 2)
        if jpy_suruga_ya != bt.cell(i, 7).value:
          bt.update_cell(i, 7, jpy_suruga_ya)
        if jpy_suruga_ya != bt.cell(i, 8).value:
          bt.update_cell(i, 8, usd_suruga_ya)
      except:
        bt.update_cell(i, 7, "err")
    else:
      if bt.cell(i, 7).value != "-":
        bt.update_cell(i, 7, "-")
      if bt.cell(i, 8).value != "-":
        bt.update_cell(i, 8, "-")

def amazon_jp(range):
  for i in range:
    time.sleep(2.5)
    print(bt.cell(i, 1).value)
    URL_amazon_jp = bt.cell(i, 39).value
    if URL_amazon_jp:
      page_amazon_jp = requests.get(URL_amazon_jp, headers=headers)
      soup_amazon_jp = BeautifulSoup(page_amazon_jp.content, 'lxml')
      try:
        price_amazon_jp = soup_amazon_jp.find(id="priceblock_ourprice").text
        jpy_amazon_jp = int(price_amazon_jp.replace('¥', '').replace(',', ''))
        usd_amazon_jp = round((c.convert('JPY', 'USD', jpy_amazon_jp)), 2)
        if jpy_amazon_jp != bt.cell(i, 9).value:
          bt.update_cell(i, 9, jpy_amazon_jp)
        if jpy_amazon_jp != bt.cell(i, 10).value:
          bt.update_cell(i, 10, usd_amazon_jp)
      except:
        bt.update_cell(i, 10, "error")
    else:
      if bt.cell(i, 9).value != "-":
        bt.update_cell(i, 9, "-")
      if bt.cell(i, 10).value != "-":
        bt.update_cell(i, 10, "-")

def ebay_jp(range):
  for i in range:
    time.sleep(2.5)
    print(bt.cell(i, 1).value)
    URL_ebay_jp = bt.cell(i, 41).value
    if URL_ebay_jp:
      page_ebay_jp = requests.get(URL_ebay_jp, headers=headers)
      soup_ebay_jp = BeautifulSoup(page_ebay_jp.content, 'lxml')
      try:
        price_ebay_jp = soup_ebay_jp.find(id="prcIsum").get('content')
        usd_ebay_jp = float(price_ebay_jp)
        jpy_ebay_jp = round((c.convert('USD', 'JPY', usd_ebay_jp)))
        if jpy_ebay_jp != bt.cell(i, 11).value:
          bt.update_cell(i, 11, jpy_ebay_jp)
        if jpy_ebay_jp != bt.cell(i, 12).value:
          bt.update_cell(i, 12, usd_ebay_jp)
      except:
        bt.update_cell(i, 12, "error")
    else:
      if bt.cell(i, 11).value != "-":
        bt.update_cell(i, 11, "-")
      if bt.cell(i, 12).value != "-":
        bt.update_cell(i, 12, "-")

def total_cards(range):
  for i in range:
    time.sleep(2.5)
    print(bt.cell(i, 1).value)
    URL_total_cards = bt.cell(i, 50).value
    if URL_total_cards:
      page_total_cards = requests.get(URL_total_cards, headers=headers)
      soup_total_cards = BeautifulSoup(page_total_cards.content, 'lxml')
      try:
        price_total_cards = soup_total_cards.select('meta[itemprop="price"]')[0].get('content')
        gbp_total_cards = float(price_total_cards)
        usd_total_cards = round((c.convert('GBP', 'USD', gbp_total_cards)), 2)
        if usd_total_cards != bt.cell(i, 23).value:
          bt.update_cell(i, 23, usd_total_cards)
      except:
        bt.update_cell(i, 23, "error")
    else:
      if bt.cell(i, 23).value != "-":
        bt.update_cell(i, 23, "-")

def geekittude(range):
  for i in range:
    time.sleep(2.5)
    print(bt.cell(i, 1).value)
    URL_geekittude = bt.cell(i, 51).value
    if URL_geekittude:
      page_geekittude = requests.get(URL_geekittude, headers=headers)
      soup_geekittude = BeautifulSoup(page_geekittude.content, 'lxml')
      try:
        price_geekittude = soup_geekittude.select('span[class="price"]')[0].text
        usd_geekittude = float(price_geekittude.replace('$', ''))
        if usd_geekittude != bt.cell(i, 24).value:
          bt.update_cell(i, 24, usd_geekittude)
      except:
        bt.update_cell(i, 24, "error")
    else:
      if bt.cell(i, 24).value != "-":
        bt.update_cell(i, 24, "-")

BT1 = range(3, 137)
BT2 = range(137, 266)
BT3 = range(266, 396)
BT4 = range(396, 532)

# yuyu_tei(BT4)
# suruga_ya(BT4)
amazon_jp(BT4)
# ebay_jp(BT2)