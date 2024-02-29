# pip install python-binance
# pip install matplotlib
from binance import Client
import matplotlib.pyplot as plt

BTC_AMOUNT = 0.2
ETH_AMOUNT = 2
AVAX_AMOUNT = 100
DOT_AMOUNT = 500
MATIC_AMOUNT = 5000
SOL_AMOUNT = 80


binance_client = Client()

def get_ticker_price(symbol: str):
    ticker_data = binance_client.get_ticker(symbol=symbol)
    return float(ticker_data['lastPrice'])

coins = ['BTC', 'ETH', 'AVAX', 'DOT', 'MATIC', 'SOL']
prices = {coin:get_ticker_price(f'{coin}USDT') for coin in coins}

myCoins = [prices[coin] * globals()[f'{coin}_AMOUNT'] for coin in coins]
tot_amount = round(sum(myCoins), 1)

plt.pie(myCoins, labels=coins)
plt.legend(title=f'Total Amount: {tot_amount}', loc='upper left')
plt.show()

