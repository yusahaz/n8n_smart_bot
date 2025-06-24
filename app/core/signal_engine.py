from app.core.patterns import get_all_detectors
from app.core.indicators import get_all_indicators
from app.core.optimizer import optimize_strategy

def generate_signals(df, config):
    matched_patterns = []
    matched_indicators = []

    # 📌 Formasyon kontrolü
    patterns = config.get("patterns", [])
    for detector in get_all_detectors():
        if detector.name() in patterns:
            if detector.detect(df):
                matched_patterns.append(detector.name())

    # 📌 İndikatör kontrolü
    indicators = config.get("indicators", [])
    for indicator in get_all_indicators():
        if indicator.name() in indicators:
            indicator.calculate(df)
            matched_indicators.append(indicator.name())

    # 📌 Basit backtest sonucu (örnekleme)
    backtest_result = {
        "win_rate": 0.7,  # örnek değerler, gerçek backtest modülünden alınmalı
        "liquidation_rate": 0.015,
        "net_pnl": 0.2
    }

    # 📌 Optimizasyon
    optimization = optimize_strategy(backtest_result)

    # 📌 Sonuç
    result = {
        **backtest_result,
        **optimization,
        "matched_patterns": matched_patterns,
        "matched_indicators": matched_indicators
    }

    return result
