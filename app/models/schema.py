from pydantic import BaseModel
from typing import List, Dict

class BacktestRequest(BaseModel):
    candles: List[List[float]]  # OHLCV
    config: Dict  # Dinamik config (ör. aktif indikatörler, patternler)

class BacktestResult(BaseModel):
    win_rate: float
    liquidation_rate: float
    net_pnl: float
    recommended_leverage: int
    trailing_stop_trigger: float
    trailing_stop_callback: float
    matched_patterns: List[str]
    matched_indicators: List[str]
