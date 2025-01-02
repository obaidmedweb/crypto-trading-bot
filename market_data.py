import ccxt
import pandas as pd
import numpy as np
from config import API_KEY, API_SECRET, TRADING_SYMBOL

class MarketData:
    def __init__(self):
        self.exchange = ccxt.binance({
            'apiKey': API_KEY,
            'secret': API_SECRET,
            'enableRateLimit': True
        })

    def get_historical_data(self, timeframe='1h', limit=100):
        """
        Fetch historical OHLCV data from Binance
        """
        try:
            ohlcv = self.exchange.fetch_ohlcv(TRADING_SYMBOL, timeframe, limit=limit)
            df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            return df
        except Exception as e:
            print(f"Error fetching historical data: {e}")
            return None

    def get_current_price(self):
        """
        Get current price for the trading pair
        """
        try:
            ticker = self.exchange.fetch_ticker(TRADING_SYMBOL)
            return ticker['last']
        except Exception as e:
            print(f"Error fetching current price: {e}")
            return None

    def get_account_balance(self):
        """
        Get account balance
        """
        try:
            balance = self.exchange.fetch_balance()
            return balance
        except Exception as e:
            print(f"Error fetching account balance: {e}")
            return None
