import lxml
import requests
from bs4 import BeautifulSoup
from forex_python.converter import CurrencyRates

c = CurrencyRates()
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}


URL_amazon_jp = 'https://www.amazon.co.jp/gp/product/B08JVTQVMS'
page_amazon_jp = requests.get(URL_amazon_jp, headers=headers)
soup_amazon_jp = BeautifulSoup(page_amazon_jp.content, 'lxml')
price_amazon_jp = soup_amazon_jp.find(id="priceblock_ourprice").text
jpy_amazon_jp = int(price_amazon_jp.replace('￥', '').replace(',', ''))

print(c.convert('JPY', 'USD', jpy_amazon_jp))
# print(soup.prettify())

