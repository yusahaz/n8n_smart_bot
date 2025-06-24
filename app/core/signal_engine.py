from app.core.indicators import calculate_indicators
from app.core.patterns import detect_patterns
from app.core.optimizer import optimize_trailing_stop

def generate_signals(df, config):
    indicators_result = calculate_indicators(df, config.get("indicators", []))
    patterns_result = detect_patterns(df, config.get("patterns", []))
    optimized = optimize_trailing_stop(df, indicators_result, patterns_result)
    return optimized
