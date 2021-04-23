# https://testnet.binance.vision/
# Binance test alım satımları yapılabilecek url. Ben testnet kullanmayacağım.

# https://python-binance.readthedocs.io/en/latest/
# Bu linkten api dökümanlarına ulaşabiliyoruz. Hadi başlayalım.

# pip install python-binance
from binance.client import Client
api_key = 'xasdqwe123141'
api_secret = '12315afqer1236'
client = Client(api_key, api_secret)
# api dökümanlarındaki constant'ları buraya yapıştırmak doğru olur. Alım satım vs sırasında lazım oluyor.
# https://python-binance.readthedocs.io/en/latest/constants.html

# Hesabımdaki coinlerimi görmek için kullandım. 
get_balance = client.get_account()
for bal in get_balance['balances']:
    if float(bal['free']) != 0.0:
        print(bal['asset'],float(bal['free']) + float(bal['locked']))
#burada free kullanılabilir durumdaki miktarı,locked de emir verilip gerçekleşmesini bekleyen miktarı gösteriyor. Ben 2 sini topladım output şöyle oldu
BNB 9.979e-05
USDT 407.81711766999996
BUSD 99.99

# get balance for a specific asset only (BTC)
print(client.get_asset_balance(asset='BTC'))
# output => {'asset': 'BTC', 'free': '0.00000000', 'locked': '0.00000000'} demekki hiç btc yok elimde.

# get latest price from Binance API for 1 coin
btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
# print full output (dictionary)
print(btc_price)
# output => {'symbol': 'BTCUSDT', 'price': '47845.00000000'}


# tüm coin paritelerini ve değerlerini öğren!!!
trade_info = client.get_all_tickers() 
for ti in trade_info:
    if 'USDT' in ti['symbol']:
        print(ti['symbol'], ":", ti['price'])
# outputs
BTCUSDT : 52175.66000000
ETHUSDT : 2440.84000000
BNBUSDT : 512.10660000
BCCUSDT : 448.70000000
NEOUSDT : 92.83200000
LTCUSDT : 262.40000000
QTUMUSDT : 14.67500000
ADAUSDT : 1.19366000
XRPUSDT : 1.26797000
EOSUSDT : 6.21320000


#Bir coin Paritesinde anlık fiyat çeker.
tickers = client.get_ticker(symbol = 'BTCUSDT')
print(tickers)
# output
{'symbol': 'BTCUSDT', 'priceChange': '-4617.70000000', 'priceChangePercent': '-8.497', 'weightedAvgPrice': '52101.35950833', 'prevClosePrice': '54342.78000000', 'lastPrice': '49725.08000000', 'lastQty': '0.46645700', 'bidPrice': '49728.14000000', 'bidQty': '0.65254300', 'askPrice': '49728.15000000', 'askQty': '0.20310000', 'openPrice': '54342.78000000', 'highPrice': '55521.48000000', 'lowPrice': '48443.01000000', 'volume': '131119.02462200', 'quoteVolume': '6831479440.21269339', 'openTime': #1619070677386, 'closeTime': 1619157077386, 'firstId': 784105253, 'lastId': 787477402, 'count': 3372150}
# Eğer print(tickers['bidPrice']) kullansaydım direk o anki fiyatı verirdi.
 
 
#al limit emri
order = client.order_limit_buy(
    symbol='BARUSDT',
    quantity=2.32,
    price='43.1')
 
#sat limit emri
order = client.order_limit_sell(
    symbol='BARUSDT',
    quantity=2.32,
    price='43.1')
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
