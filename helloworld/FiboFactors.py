class FiboFactors:
    def __init__(self,x,a,b,c,d):
        self.x = x
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.xab = (abs(b - a) / max(0.01, abs(x - a)))
        self.xad = (abs(a - d) / max(0.01, abs(x - a)))
        self.abc = (abs(b - c) / max(0.01, abs(a - b)))
        self.bcd = (abs(c - d) / max(0.01, abs(b - c)))
