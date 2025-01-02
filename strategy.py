import pandas as pd
import numpy as np
import ta
from config import RSI_PERIOD, RSI_OVERBOUGHT, RSI_OVERSOLD, EMA_FAST, EMA_SLOW

class TradingStrategy:
    def __init__(self):
        pass

    def calculate_indicators(self, df):
        """
        Calculate technical indicators
        """
        # Calculate RSI
        df['RSI'] = ta.momentum.RSIIndicator(df['close'], window=RSI_PERIOD).rsi()
        
        # Calculate EMAs
        df['EMA_fast'] = ta.trend.EMAIndicator(df['close'], window=EMA_FAST).ema_indicator()
        df['EMA_slow'] = ta.trend.EMAIndicator(df['close'], window=EMA_SLOW).ema_indicator()
        
        return df

    def generate_signals(self, df):
        """
        Generate trading signals based on technical indicators
        """
        df = self.calculate_indicators(df)
        
        # Initialize signals column
        df['signal'] = 0
        
        # Generate buy signals
        buy_conditions = (
            (df['RSI'] < RSI_OVERSOLD) &  # RSI oversold
            (df['EMA_fast'] > df['EMA_slow'])  # Golden cross
        )
        df.loc[buy_conditions, 'signal'] = 1
        
        # Generate sell signals
        sell_conditions = (
            (df['RSI'] > RSI_OVERBOUGHT) |  # RSI overbought
            (df['EMA_fast'] < df['EMA_slow'])  # Death cross
        )
        df.loc[sell_conditions, 'signal'] = -1
        
        return df

    def should_trade(self, df):
        """
        Determine if we should make a trade based on the latest signals
        """
        if len(df) == 0:
            return 0
            
        latest_signal = df['signal'].iloc[-1]
        return latest_signal  # 1 for buy, -1 for sell, 0 for hold
