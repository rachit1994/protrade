from Candle import Candle
import numpy as np


def isBat(_mode, fibonums):
    _xab = fibonums.xab >= 0.382 and fibonums.xab <= 0.5
    _abc = fibonums.abc >= 0.382 and fibonums.abc <= 0.886
    _bcd = fibonums.bcd >= 1.618 and fibonums.bcd <= 2.618
    _xad = fibonums.xad <= 0.618 and fibonums.xad <= 1.000  # 0.886
    return _xab and _abc and _bcd and _xad and (fibonums.d < fibonums.c if _mode == 1 else fibonums.d > fibonums.c)


def isAntiBat(_mode, fibonums):
    _xab = fibonums.xab >= 0.500 and fibonums.xab <= 0.886  # 0.618
    _abc = fibonums.abc >= 1.000 and fibonums.abc <= 2.618  # 1.13 --> 2.618
    _bcd = fibonums.bcd >= 1.618 and fibonums.bcd <= 2.618  # 2.0  --> 2.618
    _xad = fibonums.xad >= 0.886 and fibonums.xad <= 1.000  # 1.13
    return _xab and _abc and _bcd and _xad and (fibonums.d < fibonums.c if _mode == 1 else fibonums.d > fibonums.c)


def isAltBat(_mode, fibonums):
    _xab = fibonums.xab <= 0.382
    _abc = fibonums.abc >= 0.382 and fibonums.abc <= 0.886
    _bcd = fibonums.bcd >= 2.0 and fibonums.bcd <= 3.618
    _xad = fibonums.xad <= 1.13
    return _xab and _abc and _bcd and _xad and (fibonums.d < fibonums.c if _mode == 1 else fibonums.d > fibonums.c)


def isButterfly(_mode, fibonums):
    _xab = fibonums.xab <= 0.786
    _abc = fibonums.abc >= 0.382 and fibonums.abc <= 0.886
    _bcd = fibonums.bcd >= 1.618 and fibonums.bcd <= 2.618
    _xad = fibonums.xad >= 1.27 and fibonums.xad <= 1.618
    return _xab and _abc and _bcd and _xad and (fibonums.d < fibonums.c if _mode == 1 else fibonums.d > fibonums.c)


def isAntiButterfly(_mode, fibonums):
    _xab = fibonums.xab >= 0.236 and fibonums.xab <= 0.886  # 0.382 - 0.618
    _abc = fibonums.abc >= 1.130 and fibonums.abc <= 2.618  # 1.130 - 2.618
    _bcd = fibonums.bcd >= 1.000 and fibonums.bcd <= 1.382  # 1.27
    _xad = fibonums.xad >= 0.500 and fibonums.xad <= 0.886  # 0.618 - 0.786
    return _xab and _abc and _bcd and _xad and (fibonums.d < fibonums.c if _mode == 1 else fibonums.d > fibonums.c)


def isABCD(_mode, fibonums):
    _abc = fibonums.abc >= 0.382 and fibonums.abc <= 0.886
    _bcd = fibonums.bcd >= 1.13 and fibonums.bcd <= 2.618
    return _abc and _bcd and (fibonums.d < fibonums.c if _mode == 1 else fibonums.d > fibonums.c)


def isGartley(_mode, fibonums):
    _xab = fibonums.xab >= 0.5 and fibonums.xab <= 0.618  # 0.618
    _abc = fibonums.abc >= 0.382 and fibonums.abc <= 0.886
    _bcd = fibonums.bcd >= 1.13 and fibonums.bcd <= 2.618
    _xad = fibonums.xad >= 0.75 and fibonums.xad <= 0.875  # 0.786
    return _xab and _abc and _bcd and _xad and (fibonums.d < fibonums.c if _mode == 1 else fibonums.d > fibonums.c)


def isAntiGartley(_mode, fibonums):
    _xab = fibonums.xab >= 0.500 and fibonums.xab <= 0.886  # 0.618 -> 0.786
    _abc = fibonums.abc >= 1.000 and fibonums.abc <= 2.618  # 1.130 -> 2.618
    _bcd = fibonums.bcd >= 1.500 and fibonums.bcd <= 5.000  # 1.618
    _xad = fibonums.xad >= 1.000 and fibonums.xad <= 5.000  # 1.272
    return _xab and _abc and _bcd and _xad and (fibonums.d < fibonums.c if _mode == 1 else fibonums.d > fibonums.c)


def isCrab(_mode, fibonums):
    _xab = fibonums.xab >= 0.500 and fibonums.xab <= 0.875  # 0.886
    _abc = fibonums.abc >= 0.382 and fibonums.abc <= 0.886
    _bcd = fibonums.bcd >= 2.000 and fibonums.bcd <= 5.000  # 3.618
    _xad = fibonums.xad >= 1.382 and fibonums.xad <= 5.000  # 1.618
    return _xab and _abc and _bcd and _xad and (fibonums.d < fibonums.c if _mode == 1 else fibonums.d > fibonums.c)


def isAntiCrab(_mode, fibonums):
    _xab = fibonums.xab >= 0.250 and fibonums.xab <= 0.500  # 0.276 -> 0.446
    _abc = fibonums.abc >= 1.130 and fibonums.abc <= 2.618  # 1.130 -> 2.618
    _bcd = fibonums.bcd >= 1.618 and fibonums.bcd <= 2.618  # 1.618 -> 2.618
    _xad = fibonums.xad >= 0.500 and fibonums.xad <= 0.750  # 0.618
    return _xab and _abc and _bcd and _xad and (fibonums.d < fibonums.c if _mode == 1 else fibonums.d > fibonums.c)


def isShark(_mode, fibonums):
    _xab = fibonums.xab >= 0.500 and fibonums.xab <= 0.875  # 0.5 --> 0.886
    _abc = fibonums.abc >= 1.130 and fibonums.abc <= 1.618  #
    _bcd = fibonums.bcd >= 1.270 and fibonums.bcd <= 2.240  #
    _xad = fibonums.xad >= 0.886 and fibonums.xad <= 1.130  # 0.886 --> 1.13
    return _xab and _abc and _bcd and _xad and (fibonums.d < fibonums.c if _mode == 1 else fibonums.d > fibonums.c)


def isAntiShark(_mode, fibonums):
    _xab = fibonums.xab >= 0.382 and fibonums.xab <= 0.875  # 0.446 --> 0.618
    _abc = fibonums.abc >= 0.500 and fibonums.abc <= 1.000  # 0.618 --> 0.886
    _bcd = fibonums.bcd >= 1.250 and fibonums.bcd <= 2.618  # 1.618 --> 2.618
    _xad = fibonums.xad >= 0.500 and fibonums.xad <= 1.250  # 1.130 --> 1.130
    return _xab and _abc and _bcd and _xad and (fibonums.d < fibonums.c if _mode == 1 else fibonums.d > fibonums.c)


def is5o(_mode, fibonums):
    _xab = fibonums.xab >= 1.13 and fibonums.xab <= 1.618
    _abc = fibonums.abc >= 1.618 and fibonums.abc <= 2.24
    _bcd = fibonums.bcd >= 0.5 and fibonums.bcd <= 0.625  # 0.5
    _xad = fibonums.xad >= 0.0 and fibonums.xad <= 0.236  # negative?
    return _xab and _abc and _bcd and _xad and (fibonums.d < fibonums.c if _mode == 1 else fibonums.d > fibonums.c)


def isWolf(_mode, fibonums):
    _xab = fibonums.xab >= 1.27 and fibonums.xab <= 1.618
    _abc = fibonums.abc >= 0 and fibonums.abc <= 5
    _bcd = fibonums.bcd >= 1.27 and fibonums.bcd <= 1.618
    _xad = fibonums.xad >= 0.0 and fibonums.xad <= 5
    return _xab and _abc and _bcd and _xad and (fibonums.d < fibonums.c if _mode == 1 else fibonums.d > fibonums.c)


def isHnS(_mode, fibonums):
    _xab = fibonums.xab >= 2.0 and fibonums.xab <= 10
    _abc = fibonums.abc >= 0.90 and fibonums.abc <= 1.1
    _bcd = fibonums.bcd >= 0.236 and fibonums.bcd <= 0.88
    _xad = fibonums.xad >= 0.90 and fibonums.xad <= 1.1
    return _xab and _abc and _bcd and _xad and (fibonums.d < fibonums.c if _mode == 1 else fibonums.d > fibonums.c)


def isConTria(_mode, fibonums):
    _xab = fibonums.xab >= 0.382 and fibonums.xab <= 0.618
    _abc = fibonums.abc >= 0.382 and fibonums.abc <= 0.618
    _bcd = fibonums.bcd >= 0.382 and fibonums.bcd <= 0.618
    _xad = fibonums.xad >= 0.236 and fibonums.xad <= 0.764
    return _xab and _abc and _bcd and _xad and (fibonums.d < fibonums.c if _mode == 1 else fibonums.d > fibonums.c)


def isExpTria(_mode, fibonums):
    _xab = fibonums.xab >= 1.236 and fibonums.xab <= 1.618
    _abc = fibonums.abc >= 1.000 and fibonums.abc <= 1.618
    _bcd = fibonums.bcd >= 1.236 and fibonums.bcd <= 2.000
    _xad = fibonums.xad >= 2.000 and fibonums.xad <= 2.236
    return _xab and _abc and _bcd and _xad and (fibonums.d < fibonums.c if _mode == 1 else fibonums.d > fibonums.c)


def f_last_fib(_rate, fib_range, fibonums):
    return fibonums.d - (fib_range * _rate) if fibonums.d > fibonums.c else fibonums.d + (fib_range * _rate)


def calculateSz(candles, directions, altfactor):
    grouped_candles = []
    i = 0
    while i < len(candles) - altfactor + 1:
        grouped_candles.append(Candle(candles[i].date,
                                      candles[i].open,
                                      max([candles[x].high for x in range(i, i + altfactor)]),
                                      min([candles[x].low for x in range(i, i + altfactor)]),
                                      candles[i + altfactor - 1].close,
                                      candles[i].volume))
        i += altfactor
    
    sz = [None]*(altfactor)
    for i in range(1, len(grouped_candles)):
        nextsz = max(grouped_candles[i].high, grouped_candles[i - 1].high) if candles[i - 1].isup and \
                                                                              candles[i].isdown and directions[
                                                                                  i - 1] != -1 else (
            min(grouped_candles[i].low, grouped_candles[i - 1].low) if candles[i - 1].isdown and
                                                                       candles[i].isup and directions[
                                                                           i - 1] != 1 else None)
        sz += [nextsz] + [None]*(altfactor-1)
    sz += [None]*(len(candles)-len(sz))
    return sz


def line2arr(line, size=-1):
    '''
    Creates an numpy array from a backtrader line

    This method wraps the lines array in numpy. This can
    be used for conditions.
    '''
    if size <= 0:
        return np.array(line.array)
    else:
        return np.array(line.get(size=size))


def na(val):
    '''
    RETURNS
    true if x is not a valid number (x is NaN), otherwise false.
    '''
    return val != val


def nz(x, y=None):
    '''
    RETURNS
    Two args version: returns x if it's a valid (not NaN) number, otherwise y
    One arg version: returns x if it's a valid (not NaN) number, otherwise 0
    ARGUMENTS
    x (val) Series of values to process.
    y (float) Value that will be inserted instead of all NaN values in x series.
    '''
    if isinstance(x, np.generic):
        return x.fillna(y or 0)
    if x != x:
        if y is not None:
            return y
        return 0
    return x


def barssince(condition, occurrence=0):
    '''
    Impl of barssince

    RETURNS
    Number of bars since condition was true.
    REMARKS
    If the condition has never been met prior to the current bar, the function returns na.
    '''
    cond_len = len(condition)
    occ = 0
    since = 0
    res = float('nan')
    while cond_len - (since + 1) >= 0:
        cond = condition[cond_len - (since + 1)]
        # check for nan cond != cond == True when nan
        if cond and not cond != cond:
            if occ == occurrence:
                res = since
                break
            occ += 1
        since += 1
    return res


def valuewhen(condition, source, occurrence=0):
    res = 0
    since = barssince(condition, occurrence)
    print(since)
    if since is not None:
        res = source[-(since + 1)]
    return res


def alttf_to_tf_factor(interval, altinterval):
    m = {"minute": 1, "day": 1440, "3minute": 3, "5minute": 5, "10minute": 10, "15minute": 15, "30minute": 30,
         "60minute": 60}
    if m[interval] > m[altinterval]:
        raise Exception("alttf can not be less than tf")
    if m[altinterval] % m[interval]:
        raise Exception("alttf needs to be a multiple of tf")
    return m[altinterval] // m[interval]
