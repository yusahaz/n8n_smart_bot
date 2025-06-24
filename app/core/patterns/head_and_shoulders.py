from .base import PatternDetector

class HeadAndShoulders(PatternDetector):
    def name(self):
        return "head_and_shoulders"

    def detect(self, df):
        window = df.tail(50)
        highs = window['high'].values
        if len(highs) < 7:
            return False
        peaks = []
        for i in range(1, len(highs)-1):
            if highs[i] > highs[i-1] and highs[i] > highs[i+1]:
                peaks.append((i, highs[i]))
        if len(peaks) < 3:
            return False
        peaks = sorted(peaks, key=lambda x: x[1], reverse=True)[:3]
        peaks = sorted(peaks, key=lambda x: x[0])
        left, head, right = peaks
        if head[1] > left[1] and head[1] > right[1]:
            diff = abs(left[1] - right[1]) / head[1]
            return diff < 0.25
        return False
