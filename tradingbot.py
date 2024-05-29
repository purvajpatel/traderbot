from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime 
from alpaca_trade_api import REST 
from timedelta import Timedelta 
from tradingAnalysis import trader 

API_KEY = "hidden"  
API_SECRET = "hidden"  # you can get your own at https://paper-api.alpaca.markets/v2
BASE_URL = "https://paper-api.alpaca.markets/v2"

ALPACA_CREDS = {
    "API_KEY":API_KEY, 
    "API_SECRET": API_SECRET, 
    "PAPER": True
}

class WallStreetBets(Strategy): 
    def initialize(self, symbol:str="SPY", cash_at_risk:float=.05): 
        self.symbol = symbol
        self.sleeptime = "24H" 
        self.last_trade = None 
        self.cash_at_risk = cash_at_risk
        
    def position_sizing(self):
        cash = self.get_cash()
        last_price = self.get_last_price(self.symbol)
        quantity = round(cash*self.cash_at_risk / last_price,0)
        return cash, last_price, quantity
    
    def get_dates(self): 
        today = self.get_datetime()
        three_days_prior = today - Timedelta(days=3)
        return today.strftime('%Y-%m-%d'), three_days_prior.strftime('%Y-%m-%d')

    def on_trading_iteration(self):
        cash, last_price, quantity = self.position_sizing()
        trader_instance = trader('SPY')
        sentiment = trader_instance.run_trading_analysis()
        if cash > last_price: 
            if sentiment == "BUY":
                if self.last_trade == "sell": 
                    self.sell_all() 
                order = self.create_order(
                    self.symbol, 
                    quantity, 
                    "buy", 
                    type="bracket", 
                    take_profit_price=last_price*1.20, 
                    stop_loss_price=last_price*.95
                )
                self.submit_order(order) 
                self.last_trade = "buy"
            elif sentiment == "SELL": 
                if self.last_trade == "buy": 
                    self.sell_all() 
                order = self.create_order(
                    self.symbol, 
                    quantity, 
                    "sell", 
                    type="bracket", 
                    take_profit_price=last_price*.8, 
                    stop_loss_price=last_price*1.05
                )
                self.submit_order(order) 
                self.last_trade = "sell"
 
start_date = datetime(2024,4,25)
end_date = datetime(2024,5,29) 
broker = Alpaca(ALPACA_CREDS) 
strategy = WallStreetBets(name='wallstreetbets', broker=broker, 
                    parameters={"symbol":"SPY", "cash_at_risk":.5})
strategy.backtest(
    YahooDataBacktesting, 
    start_date, 
    end_date, 
    parameters={"symbol":"SPY", "cash_at_risk":.5}
)
# trader = Trader()s
# trader.add_strategy(strategy)
# trader.run_all()
