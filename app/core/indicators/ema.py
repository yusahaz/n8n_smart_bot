from .base import IndicatorCalculator
import pandas_ta as ta

class EMAIndicator(IndicatorCalculator):
    def name(self):
        return "EMA"

    def calculate(self, df):
        df['ema'] = ta.ema(df['close'], length=14)
        return df['ema']
