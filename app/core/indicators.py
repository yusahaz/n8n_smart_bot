import pandas_ta as ta

def calculate_indicators(df, indicators):
    result = []

    if "EMA" in indicators:
        df['ema9'] = ta.ema(df['close'], length=9)
        df['ema21'] = ta.ema(df['close'], length=21)
        result.append("EMA")

    if "RSI" in indicators:
        df['rsi'] = ta.rsi(df['close'], length=14)
        result.append("RSI")

    if "MACD" in indicators:
        try:
            if len(df) >= 35:  # Güvenli sınır
                macd_df = ta.macd(df['close'])
                if macd_df is not None and not macd_df.empty:
                    df['macd'] = macd_df.iloc[:, 0].fillna(0)
                    df['macdsignal'] = macd_df.iloc[:, 1].fillna(0)
                    result.append("MACD")
                else:
                    print("⚠ MACD hesaplanamadı: boş döndü")
            else:
                print("⚠ MACD için yeterli veri yok")
        except Exception as e:
            print(f"⚠ MACD hesaplama hatası: {e}")

    return result
