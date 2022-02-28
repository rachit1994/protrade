class Candle:
    def __init__(self,date,open,high,low,close,volume):
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.isup = close >= open
        self.isdown = close <= open

    def __repr__(self):
        return f"(d={self.date},\no={self.open},\nh={self.high},\nl={self.low},\nc={self.close},\nv={self.volume},\nup={self.isup},\ndn={self.isdown})"