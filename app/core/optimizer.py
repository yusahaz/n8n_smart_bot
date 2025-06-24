from app.models.schema import BacktestResult

def optimize_trailing_stop(df, indicators, patterns):
    # Burada trigger/callback kombinasyonlarını tarayıp en iyi sonucu bulacağız
    # Şimdilik örnek değerler
    return BacktestResult(
        win_rate=0.7,
        liquidation_rate=0.015,
        net_pnl=0.2,
        recommended_leverage=50,
        trailing_stop_trigger=0.6,
        trailing_stop_callback=0.2,
        matched_patterns=patterns,
        matched_indicators=indicators
    )
