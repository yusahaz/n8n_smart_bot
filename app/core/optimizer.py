from app.models.schema import BacktestResult

def optimize_trailing_stop(df, indicators, patterns):
    # Geçici sabit örnek
    return BacktestResult(
        win_rate=0.65,
        liquidation_rate=0.02,
        net_pnl=0.18,
        recommended_leverage=50,
        trailing_stop_trigger=0.6,
        trailing_stop_callback=0.2,
        matched_patterns=patterns,
        matched_indicators=indicators
    )
