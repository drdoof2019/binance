***Using the Binance WebSocket for the latest Bitcoin price***
The Binance WebSocket requires us to only send a command once to open up a stream, and then data will automatically stream over as prices get updated.

from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor

api_key = 'qwe12314'
api_secret = 'jasda61'
client = Client(api_key, api_secret)

#A dictionary has also been declared, this will hold our latest price data.
btc_price = {'error':False}

def btc_trade_history(msg):
    ''' define how to process incoming WebSocket messages '''
    if msg['e'] != 'error':
        print(msg['c'])
        btc_price['last'] = msg['c']
        btc_price['bid'] = msg['b']
        btc_price['last'] = msg['a']
    else:
        btc_price['error'] = True

# init and start the WebSocket
bsm = BinanceSocketManager(client)
conn_key = bsm.start_symbol_ticker_socket('BTCUSDT', btc_trade_history)
bsm.start()
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            # stop websocket
            bsm.stop_socket(conn_key)
            # properly terminate WebSocket
            reactor.stop()
            break
    except:
        pass

# The next step is to initialize the socket manager.
# We will call the start_symbol_ticker_socket which has similar output to the get_symbol_ticker function of the API.
# We need to pass through a symbol, which in this case is BTCUSDT. We also specify it to call our custom btc_trade_history function every time a new message comes in.
# Lastly, we just need to start the socket.
# If you’re following along, you should see a stream of prices on your screen. It should look similar to the Trade History box that is on the Binance webpage under the spot trading section.
# In a live Python trading script, you will access the data from the dictionary file outside the function as opposed to printing the data to screen from the function.
# When you’re done with the WebSocket, use the following syntax to properly terminate it:

