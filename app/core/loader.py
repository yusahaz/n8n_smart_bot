import pandas as pd

def load_data(candles):
    df = pd.DataFrame(candles, columns=["timestamp", "open", "high", "low", "close", "volume"])
    return df
