from config import STOP_LOSS_PERCENTAGE, TAKE_PROFIT_PERCENTAGE

class RiskManager:
    def __init__(self):
        self.stop_loss_pct = STOP_LOSS_PERCENTAGE
        self.take_profit_pct = TAKE_PROFIT_PERCENTAGE

    def calculate_position_size(self, balance, current_price):
        """
        Calculate appropriate position size based on account balance
        """
        # Using a conservative 2% risk per trade
        risk_per_trade = balance * 0.02
        return risk_per_trade / current_price

    def check_stop_loss(self, entry_price, current_price, position_type='long'):
        """
        Check if stop loss has been hit
        """
        if position_type == 'long':
            stop_price = entry_price * (1 - self.stop_loss_pct/100)
            return current_price <= stop_price
        else:  # short position
            stop_price = entry_price * (1 + self.stop_loss_pct/100)
            return current_price >= stop_price

    def check_take_profit(self, entry_price, current_price, position_type='long'):
        """
        Check if take profit has been hit
        """
        if position_type == 'long':
            target_price = entry_price * (1 + self.take_profit_pct/100)
            return current_price >= target_price
        else:  # short position
            target_price = entry_price * (1 - self.take_profit_pct/100)
            return current_price <= target_price

    def should_close_position(self, entry_price, current_price, position_type='long'):
        """
        Determine if position should be closed based on risk management rules
        """
        if self.check_stop_loss(entry_price, current_price, position_type):
            return True, "Stop Loss"
        if self.check_take_profit(entry_price, current_price, position_type):
            return True, "Take Profit"
        return False, None
