from .base import IndicatorCalculator
import pandas_ta as ta

class MACDIndicator(IndicatorCalculator):
    def name(self):
        return "MACD"

    def calculate(self, df):
        macd_df = ta.macd(df['close'])
        df['macd'] = macd_df['MACD_12_26_9']
        return df['macd']
