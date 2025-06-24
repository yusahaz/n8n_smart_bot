from .base import IndicatorCalculator
import pandas_ta as ta

class SuperTrendIndicator(IndicatorCalculator):
    def name(self):
        return "SuperTrend"

    def calculate(self, df):
        st = ta.supertrend(df["high"], df["low"], df["close"], length=10, multiplier=3)
        df["supertrend"] = st[f"SUPERT_10_3.0"]
        return df["supertrend"]
