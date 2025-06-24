from .base import IndicatorCalculator
import pandas_ta as ta

class RSIIndicator(IndicatorCalculator):
    def name(self):
        return "RSI"

    def calculate(self, df):
        df['rsi'] = ta.rsi(df['close'], length=14)
        return df['rsi']
