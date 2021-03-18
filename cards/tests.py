# import lxml
import requests
from bs4 import BeautifulSoup
from forex_python.converter import CurrencyRates
import schedule
import time

c = CurrencyRates()
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

URL_suruga_ya = 'https://www.suruga-ya.jp/product/detail/GG646306'
page_suruga_ya = requests.get(URL_suruga_ya, headers=headers)
soup_suruga_ya = BeautifulSoup(page_suruga_ya.content, 'lxml')
price_suruga_ya = soup_suruga_ya.find(class_="text-price-detail price-buy").text
jpy_suruga_ya = int(price_suruga_ya.replace('円 (税込)', ''))
usd_suruga_ya = round((c.convert('JPY', 'USD', jpy_suruga_ya)), 2)

print(jpy_suruga_ya)

def job():
    print(usd_suruga_ya)

schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
