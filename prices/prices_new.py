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

gs = gspread.service_account(filename='prices\creds.json')
spreadsheet = gs.open('DTCGprices')
sheet1 = spreadsheet.sheet1

def yuyu_tei():
  for i in range(3, 150):
    time.sleep(2.5)
    URL_yuyu_tei = sheet1.cell(i, 37).value
    if URL_yuyu_tei:
      page_yuyu_tei = requests.get(URL_yuyu_tei, headers=headers)
      soup_yuyu_tei = BeautifulSoup(page_yuyu_tei.content, 'lxml')
      price_yuyu_tei = soup_yuyu_tei.find(class_="price").b.text
      jpy_yuyu_tei = int(price_yuyu_tei.replace('円', ''))
      usd_yuyu_tei = round((c.convert('JPY', 'USD', jpy_yuyu_tei)), 2)
      if jpy_yuyu_tei != sheet1.cell(i, 5).value:
        sheet1.update_cell(i, 5, jpy_yuyu_tei)
      if jpy_yuyu_tei != sheet1.cell(i, 6).value:
        sheet1.update_cell(i, 6, usd_yuyu_tei)
    else:
      if sheet1.cell(i, 5).value != "-":
        sheet1.update_cell(i, 5, "-")
      if sheet1.cell(i, 6).value != "-":
        sheet1.update_cell(i, 6, "-")

def suruga_ya():
  for i in range(3, 150):
    time.sleep(2.5)
    URL_suruga_ya = sheet1.cell(i, 38).value
    if URL_suruga_ya:
      page_suruga_ya = requests.get(URL_suruga_ya, headers=headers)
      soup_suruga_ya = BeautifulSoup(page_suruga_ya.content, 'lxml')
      try:
        price_suruga_ya = soup_suruga_ya.find(class_="text-price-detail price-buy").text
        jpy_suruga_ya = int(price_suruga_ya.replace('円 (税込)', '').replace(',', ''))
        usd_suruga_ya = round((c.convert('JPY', 'USD', jpy_suruga_ya)), 2)
        if jpy_suruga_ya != sheet1.cell(i, 7).value:
          sheet1.update_cell(i, 7, jpy_suruga_ya)
        if jpy_suruga_ya != sheet1.cell(i, 8).value:
          sheet1.update_cell(i, 8, usd_suruga_ya)
      except:
        sheet1.update_cell(i, 7, "err")
    else:
      if sheet1.cell(i, 7).value != "-":
        sheet1.update_cell(i, 7, "-")
      if sheet1.cell(i, 8).value != "-":
        sheet1.update_cell(i, 8, "-")

def amazon_jp():
  for i in range(3, 150):
    time.sleep(2.5)
    URL_amazon_jp = sheet1.cell(i, 39).value
    if URL_amazon_jp:
      page_amazon_jp = requests.get(URL_amazon_jp, headers=headers)
      soup_amazon_jp = BeautifulSoup(page_amazon_jp.content, 'lxml')
      try:
        price_amazon_jp = soup_amazon_jp.find(id="priceblock_ourprice").text
        jpy_amazon_jp = int(price_amazon_jp.replace('¥', '').replace(',', ''))
        usd_amazon_jp = round((c.convert('JPY', 'USD', jpy_amazon_jp)), 2)
        if jpy_amazon_jp != sheet1.cell(i, 9).value:
          sheet1.update_cell(i, 9, jpy_amazon_jp)
        if jpy_amazon_jp != sheet1.cell(i, 10).value:
          sheet1.update_cell(i, 10, usd_amazon_jp)
      except:
        sheet1.update_cell(i, 10, "error")
    else:
      if sheet1.cell(i, 9).value != "-":
        sheet1.update_cell(i, 9, "-")
      if sheet1.cell(i, 10).value != "-":
        sheet1.update_cell(i, 10, "-")

def ebay_jp():
  for i in range(3, 150):
    time.sleep(2.5)
    URL_ebay_jp = sheet1.cell(i, 41).value
    if URL_ebay_jp:
      page_ebay_jp = requests.get(URL_ebay_jp, headers=headers)
      soup_ebay_jp = BeautifulSoup(page_ebay_jp.content, 'lxml')
      try:
        price_ebay_jp = soup_ebay_jp.find(id="prcIsum").get('content')
        usd_ebay_jp = float(price_ebay_jp)
        jpy_ebay_jp = round((c.convert('USD', 'JPY', usd_ebay_jp)))
        if jpy_ebay_jp != sheet1.cell(i, 11).value:
          sheet1.update_cell(i, 11, jpy_ebay_jp)
        if jpy_ebay_jp != sheet1.cell(i, 12).value:
          sheet1.update_cell(i, 12, usd_ebay_jp)
      except:
        sheet1.update_cell(i, 12, "error")
    else:
      if sheet1.cell(i, 11).value != "-":
        sheet1.update_cell(i, 11, "-")
      if sheet1.cell(i, 12).value != "-":
        sheet1.update_cell(i, 12, "-")

ebay_jp()