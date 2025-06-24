from fastapi import FastAPI
from app.models.schema import BacktestRequest, BacktestResult
from app.core.loader import load_data
from app.core.signal_engine import generate_signals

app = FastAPI(title="Smart Backtest Engine")

@app.post("/backtest", response_model=BacktestResult)
async def run_backtest(request: BacktestRequest):
    df = load_data(request.candles)
    result = generate_signals(df, request.config)
    return result
