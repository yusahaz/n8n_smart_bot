from .ema import EMAIndicator
from .rsi import RSIIndicator
from .macd import MACDIndicator
from .alma import ALMAIndicator
from .supertrend import SuperTrendIndicator

def get_all_indicators():
    return [
        EMAIndicator(),
        RSIIndicator(),
        MACDIndicator(),
        ALMAIndicator(),
        SuperTrendIndicator()
    ]
