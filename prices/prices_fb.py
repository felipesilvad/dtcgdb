import pyrebase
import gspread
import requests
import time
import datetime
import lxml
from forex_python.converter import CurrencyRates

config = {
  "apiKey": "AIzaSyDb38S-7VjMuaON7Yehmfa8jCFqexLCXZc",
  "authDomain": "dtcgprices.firebaseapp.com",
  "databaseURL": "https://dtcgprices-default-rtdb.firebaseio.com",
  "projectId": "dtcgprices",
  "storageBucket": "dtcgprices.appspot.com",
  "messagingSenderId": "798394460561",
  "appId": "1:798394460561:web:fbd9a44b628b0ce4dad230",
  "measurementId": "G-PFRXJB95PZ"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

dbcard = db.child('BT1-001').child('2021').child('04').child('01').get().val()

print(dbcard[en]['ebay'][0])

c = CurrencyRates(force_decimal=False)
gs = gspread.service_account(filename='prices/creds.json')
spreadsheet = gs.open('DTCGprices')
bt = spreadsheet.sheet1

BT1 = range(3, 137)

# for i in BT1:
#   time.sleep(30)
#   card = bt.cell(i, 1).value
#   # JP
#   try: avg_jp_jpy = int(bt.cell(i, 3).value)
#   except: avg_jp_jpy = 'error'
#   try: avg_jp_usd = round((c.convert('JPY', 'USD', avg_jp_jpy)), 2)
#   except: avg_jp_usd = 'error'
#   try: yuyu_tei_jpy = int(bt.cell(i, 5).value)
#   except: yuyu_tei_jpy = 'error'
#   try: yuyu_tei_usd = round((c.convert('JPY', 'USD', yuyu_tei_jpy)), 2)
#   except: yuyu_tei_usd = 'error'
#   try: yuyu_tei_url = bt.cell(i, 37).value
#   except: yuyu_tei_url = 'error'
#   try: suruga_ya_jpy = int(bt.cell(i, 7).value)
#   except: suruga_ya_jpy = 'error'
#   try: suruga_ya_usd = round((c.convert('JPY', 'USD', suruga_ya_jpy)), 2)
#   except: suruga_ya_usd = 'error'
#   try: suruga_ya_url = bt.cell(i, 38).value
#   except: suruga_ya_url = 'error'
#   try: amazon_jp_jpy = int(bt.cell(i, 9).value)
#   except: amazon_jp_jpy = 'error'
#   try: amazon_jp_usd = round((c.convert('JPY', 'USD', amazon_jp_jpy)), 2)
#   except: amazon_jp_usd = 'error'
#   try: amazon_jp_url = bt.cell(i, 40).value
#   except: amazon_jp_url = 'error'
#   try: ebay_jp_jpy = int(bt.cell(i, 11).value)
#   except: ebay_jp_jpy = 'error'
#   try: ebay_jp_usd = round((c.convert('JPY', 'USD', ebay_jp_jpy)), 2)
#   except: ebay_jp_usd = 'error'
#   try: ebay_jp_url = bt.cell(i, 40).value
#   except: ebay_jp_url = 'error'
#   # EN
#   try: avg_en = float(bt.cell(i, 20).value)
#   except: avg_en = 'error'
#   try: ebay = float(bt.cell(i, 21).value)
#   except: ebay = 'error'
#   try: ebay_url = bt.cell(i, 49).value
#   except: ebay_url = 'error'
#   try: totalcards = float(bt.cell(i, 23).value)
#   except: totalcards = 'error'
#   try: totalcards_url = bt.cell(i, 50).value
#   except: totalcards_url = 'error'
#   try: geekittude = float(bt.cell(i, 24).value)
#   except: geekittude = 'error'
#   try: geekittude_url = bt.cell(i, 51).value
#   except: geekittude_url = 'error'
#   try: tcg_player = float(bt.cell(i, 25).value)
#   except: tcg_player = 'error'
#   db.child(card).set({
#     "2021": {
#       "04": {
#         "01": {
#           "jp": {
#             'avg': [avg_jp_jpy, avg_jp_usd],
#             'yuyu_tei': [yuyu_tei_jpy, yuyu_tei_usd, yuyu_tei_url],
#             'suruga_ya': [suruga_ya_jpy, suruga_ya_usd, suruga_ya_url],
#             'amazon': [amazon_jp_jpy, amazon_jp_usd, amazon_jp_url],
#             'ebay': [ebay_jp_jpy, ebay_jp_usd, ebay_jp_url],
#           },
#           "en": {
#             'avg': avg_en,
#             'ebay': [ebay, ebay_url],
#             'totalcards': [totalcards, totalcards_url],
#             'geekittude': [geekittude, geekittude_url],
#             'tcg_player': tcg_player,
#           }
#         }
#       }
#     }
#   })