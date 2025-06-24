def optimize_strategy(backtest_results):
    win_rate = backtest_results.get("win_rate", 0)
    liquidation_rate = backtest_results.get("liquidation_rate", 0)

    # Leverage hesapla
    max_leverage = 100  # örnek üst limit
    recommended_leverage = max(1, int((win_rate - liquidation_rate) * max_leverage))
    recommended_leverage = min(recommended_leverage, max_leverage)

    # Trailing stop trigger
    if win_rate > 0.7:
        trailing_trigger = 0.6
        trailing_callback = 0.2
    elif win_rate > 0.5:
        trailing_trigger = 0.4
        trailing_callback = 0.1
    else:
        trailing_trigger = 0.2
        trailing_callback = 0.05

    return {
        "recommended_leverage": recommended_leverage,
        "trailing_stop_trigger": trailing_trigger,
        "trailing_stop_callback": trailing_callback
    }
