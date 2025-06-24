from .base import IndicatorCalculator
import pandas_ta as ta

class ALMAIndicator(IndicatorCalculator):
    def name(self):
        return "ALMA"

    def calculate(self, df):
        df["alma"] = ta.alma(df["close"], length=10, offset=0.85, sigma=6)
        return df["alma"]
