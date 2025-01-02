from market_data import MarketData
from strategy import TradingStrategy
from risk_manager import RiskManager
from config import TRADING_SYMBOL, QUANTITY
import time

class CryptoTrader:
    def __init__(self):
        self.market_data = MarketData()
        self.strategy = TradingStrategy()
        self.risk_manager = RiskManager()
        self.position = None
        self.entry_price = None

    def execute_trade(self, side, quantity):
        """
        Execute trade on the exchange
        """
        try:
            if side == 'buy':
                order = self.market_data.exchange.create_market_buy_order(TRADING_SYMBOL, quantity)
            else:
                order = self.market_data.exchange.create_market_sell_order(TRADING_SYMBOL, quantity)
            return order
        except Exception as e:
            print(f"Error executing trade: {e}")
            return None

    def run(self):
        """
        Main trading loop
        """
        print(f"Starting trading bot for {TRADING_SYMBOL}")
        
        while True:
            try:
                # Get market data
                df = self.market_data.get_historical_data()
                if df is None:
                    continue

                current_price = self.market_data.get_current_price()
                if current_price is None:
                    continue

                # Generate trading signals
                df = self.strategy.generate_signals(df)
                signal = self.strategy.should_trade(df)

                # Check if we have an open position
                if self.position:
                    # Check if we should close the position
                    should_close, reason = self.risk_manager.should_close_position(
                        self.entry_price, 
                        current_price, 
                        self.position
                    )
                    
                    if should_close:
                        print(f"Closing position: {reason}")
                        self.execute_trade('sell' if self.position == 'long' else 'buy', QUANTITY)
                        self.position = None
                        self.entry_price = None
                
                # No position is open, check for new trades
                elif signal != 0:
                    # Calculate position size
                    balance = self.market_data.get_account_balance()
                    if balance:
                        usdt_balance = balance['total'].get('USDT', 0)
                        position_size = self.risk_manager.calculate_position_size(usdt_balance, current_price)
                        
                        if signal == 1:  # Buy signal
                            print(f"Opening long position at {current_price}")
                            order = self.execute_trade('buy', position_size)
                            if order:
                                self.position = 'long'
                                self.entry_price = current_price
                        
                        elif signal == -1:  # Sell signal
                            print(f"Opening short position at {current_price}")
                            order = self.execute_trade('sell', position_size)
                            if order:
                                self.position = 'short'
                                self.entry_price = current_price

                # Sleep for a while before next iteration
                time.sleep(60)  # Check every minute

            except Exception as e:
                print(f"Error in main loop: {e}")
                time.sleep(60)  # Wait before retrying

if __name__ == "__main__":
    trader = CryptoTrader()
    trader.run()
