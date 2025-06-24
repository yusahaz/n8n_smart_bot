from fastapi import FastAPI
from app.models.schema import BacktestRequest, BacktestResult
from app.core.loader import load_data
from app.core.signal_engine import generate_signals

app = FastAPI(
    title="Smart Crypto Backtest Engine",
    description="""
    🚀 Gelişmiş bir backtest motoru.

    - Çoklu indikatör desteği (EMA, RSI, MACD, vb)
    - Pattern tanıma (Head-and-Shoulders, Triangle, Flag, vb)
    - Trailing stop ve kaldıraç optimizasyonu
    """,
    version="0.1.0",
    contact={
        "name": "Yusuf Haz",
        "url": "https://github.com/yusahaz/n8n_smart_bot",
    }
)

@app.post("/backtest", response_model=BacktestResult, tags=["Backtest"])
async def run_backtest(request: BacktestRequest):
    """
    Seçilen indikatörler ve formasyonlar ile backtest çalıştırır.
    En uygun trailing stop ve kaldıraç değerlerini önerir.
    """
    df = load_data(request.candles)
    result = generate_signals(df, request.config)
    return result
