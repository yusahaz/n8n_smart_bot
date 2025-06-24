from .base import PatternDetector

class DescendingTriangle(PatternDetector):
    def name(self):
        return "descending_triangle"

    def detect(self, df):
        window = df.tail(50)
        highs = window['high'].values
        lows = window['low'].values

        if len(highs) < 5:
            return False

        high_trend = sum(1 for i in range(1, len(highs)) if highs[i] <= highs[i-1] * 1.01) >= len(highs) * 0.7
        low_flat = max(lows) - min(lows) < (0.01 * min(lows))

        return high_trend and low_flat
