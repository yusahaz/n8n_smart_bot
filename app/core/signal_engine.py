from app.core.patterns import get_all_detectors

def generate_signals(df, config):
    patterns = config.get("patterns", [])
    matched = []

    for detector in get_all_detectors():
        if detector.name() in patterns:
            if detector.detect(df):
                matched.append(detector.name())

    return matched
from app.core.patterns import get_all_detectors
from app.core.indicators import calculate_indicators

def generate_signals(df, config):
    matched_patterns = []
    matched_indicators = []

    # Formasyonları kontrol et
    patterns = config.get("patterns", [])
    for detector in get_all_detectors():
        if detector.name() in patterns:
            if detector.detect(df):
                matched_patterns.append(detector.name())
                print(f"✅ Formasyon eşleşti: {detector.name()}")
            else:
                print(f"❌ Formasyon eşleşmedi: {detector.name()}")

    # İndikatörleri hesapla
    indicators = config.get("indicators", [])
    matched_indicators = calculate_indicators(df, indicators)

    # Örnek dummy optimizer sonucu (bunu sonra gerçek hale getireceğiz)
    result = {
        "win_rate": 0.7,
        "liquidation_rate": 0.015,
        "net_pnl": 0.2,
        "recommended_leverage": 50,
        "trailing_stop_trigger": 0.6,
        "trailing_stop_callback": 0.2,
        "matched_patterns": matched_patterns,
        "matched_indicators": matched_indicators
    }

    return result
