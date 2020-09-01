import lxml
import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.co.jp/%E3%82%BC%E3%83%AB%E3%83%80%E3%81%AE%E4%BC%9D%E8%AA%AC%E3%82%B3%E3%83%B3%E3%82%B5%E3%83%BC%E3%83%882018%E3%80%90%E5%88%9D%E5%9B%9E%E6%95%B0%E9%87%8F%E7%94%9F%E7%94%A3%E9%99%90%E5%AE%9A%E7%9B%A4%E3%80%91-%E4%BB%BB%E5%A4%A9%E5%A0%82/dp/B07L45D4S5?pf_rd_r=RJZV8F55BXFVZG9KEEN3&pf_rd_p=a8c88fef-9642-4ae5-a59b-5d9ea98f265d&pd_rd_r=4d855071-295a-4704-9a3a-01fcdf746d16&pd_rd_w=dflBy&pd_rd_wg=hy703&ref_=pd_gw_bia_d0'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'lxml')

price = soup.find(id="priceblock_ourprice")
print(soup)

# URL = 'https://www.ebay.com/itm/Digimon-Puppetmon-BT2-049-USA/254674640153?_trkparms=aid%3D1110012%26algo%3DSPLICE.SOIPOST%26ao%3D1%26asc%3D20200818142651%26meid%3Dc1100450ac6d45ac86e602c865b47589%26pid%3D101196%26rk%3D3%26rkt%3D12%26mehot%3Dnone%26sd%3D254674623161%26itm%3D254674640153%26pmt%3D1%26noa%3D0%26pg%3D2047675%26algv%3DPromotedSellersOtherItemsV2&_trksid=p2047675.c101196.m2219'

# headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

# page = requests.get(URL, headers=headers)

# soup = BeautifulSoup(page.content, 'html.parser')

# price = soup.find(id="prcIsum")
# print(price)
