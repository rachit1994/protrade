from Candle import Candle
from Constants import *
from FiboFactors import FiboFactors
from functions import *
from kiteconnect import KiteConnect
from kitealgo import getkite
import csv

csv_file =  open("test.csv", 'w')

csv_writer = csv.writer(csv_file, delimiter=",")

kite = getkite()
# use kite.instruments() to fetch all instruments
instrument_token = 738561
from_data = "2020-07-01 09:00:00"
to_data = "2020-08-01 16:00:00"
# intervals: minute,day,3minute,5minute,10minute,15minute,30minute,60minute
interval = "15minute"
altTimeFrame = "60minute"
useAltTF=True
# https://kite.trade/docs/connect/v3/historical/
bardata = kite.historical_data(instrument_token=instrument_token,
                               from_date=from_data,
                               to_date=to_data,
                               interval=interval)

candles = [Candle(**x) for x in bardata]
directions = [1 if candles[x].isup else -1 for x in range(len(candles))]
sz = calculateSz(candles, directions, alttf_to_tf_factor(interval=interval, altinterval=altTimeFrame)) \
    if useAltTF else calculateSz(candles, directions, 1)
    

# for i in range(len(candles)):
#     print(f"{candles[i].date} - {candles[i].open} - dir {directions[i]} -sz {sz[i]}")

# print(directions)
# print(sz)
# sz = [(i, x) for i, x in enumerate(sz) if x]
# print(sz)
t1_buys = t1_sells = t2_buys = t2_sells = None

amount = initial_amount = 100000
shares_buycell_perdeal  = 1
stoploss_factor = 0.02
brokercost = 20
count = 0
j = 0
while count < 5 and j < len(candles):
    if sz[j]:
        count+=1
    j+=1

csv_writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'SZ', 'Direction', 'x', 'a', 'b', 'c', 'd'])
for i in range(j, len(candles)):
    # print(candles[sz[i][0]].date)
    if amount<0:
        print("!!!!!!!!!!!!")
        break
    szs = []
    for k in range(i,-1,-1):
        if sz[k]:
            szs.insert(0, sz[k])
        if len(szs) == 5:
            break

    fibonums = FiboFactors(*szs)
    curr = i
    c_open = candles[curr].open
    c_high = candles[curr].high
    c_low = candles[curr].low
    c_close = candles[curr].close
    c_date = candles[curr].date
    csv_writer.writerow([c_date, c_open, c_high, c_low, c_close, sz[i], directions[i], fibonums.x, fibonums.a, fibonums.b, fibonums.c, fibonums.d])

    fib_range = abs(fibonums.d - fibonums.c)
    fib_0000 = None if not showFib0000 else (fibonums.d - (fib_range * 0.000) if fibonums.d > fibonums.c else fibonums.d + (fib_range * 0.000))
    fib_0236 = None if not showFib0236 else (fibonums.d - (fib_range * 0.236) if fibonums.d > fibonums.c else fibonums.d + (fib_range * 0.236))
    fib_0382 = None if not showFib0382 else (fibonums.d - (fib_range * 0.382) if fibonums.d > fibonums.c else fibonums.d + (fib_range * 0.382))
    fib_0500 = None if not showFib0500 else (fibonums.d - (fib_range * 0.500) if fibonums.d > fibonums.c else fibonums.d + (fib_range * 0.500))
    fib_0618 = None if not showFib0618 else (fibonums.d - (fib_range * 0.618) if fibonums.d > fibonums.c else fibonums.d + (fib_range * 0.618))
    fib_0764 = None if not showFib0764 else (fibonums.d - (fib_range * 0.764) if fibonums.d > fibonums.c else fibonums.d + (fib_range * 0.764))
    fib_1000 = None if not showFib1000 else (fibonums.d - (fib_range * 1.000) if fibonums.d > fibonums.c else fibonums.d + (fib_range * 1.000))

    buy_patterns_00 = isABCD(1, fibonums) or isBat(1, fibonums) or isAltBat(1, fibonums) or isButterfly(1, fibonums) \
                      or isGartley(1, fibonums) or isCrab(1, fibonums) or isShark(1, fibonums) or is5o(1, fibonums) \
                      or isWolf(1, fibonums) or isHnS(1, fibonums) or isConTria(1, fibonums) or isExpTria(1, fibonums)
    buy_patterns_01 = isAntiBat(1, fibonums) or isAntiButterfly(1, fibonums) or isAntiGartley(1, fibonums)\
                      or isAntiCrab(1,fibonums) or isAntiShark(1, fibonums)
    sel_patterns_00 = isABCD(-1, fibonums) or isBat(-1, fibonums) or isAltBat(-1, fibonums) or isButterfly(-1, fibonums) \
                      or isGartley(-1, fibonums) or isCrab(-1, fibonums) or isShark(-1, fibonums) or is5o(-1, fibonums) \
                      or isWolf(-1, fibonums) or isHnS(-1, fibonums)  or isConTria(-1, fibonums) or isExpTria(-1, fibonums)
    sel_patterns_01 = isAntiBat(-1, fibonums) or isAntiButterfly(-1,fibonums)  or isAntiGartley(-1, fibonums)\
                      or isAntiCrab(-1, fibonums) or isAntiShark(-1, fibonums)
    
    # shares_buycell_perdeal = (amount*0.7)//c_close
    if not t1_buys and ((buy_patterns_00 or buy_patterns_01) and c_close <= f_last_fib(target01_ew_rate, fib_range, fibonums)):
        print(f"T1 BUY ENTRY - on {c_date} @ {c_close}")
        t1_buys = c_close
        amount = amount - (shares_buycell_perdeal*c_close) - brokercost

    if t1_buys and (c_high >= f_last_fib(target01_tp_rate, fib_range, fibonums) or c_low <= f_last_fib(
        target01_sl_rate, fib_range, fibonums)
                    # or t1_buys-c_low<= t1_buys*stoploss_factor
    ):
        print(f"T1 BUY CLOSE - on {c_date} @ {c_close}")
        t1_buys = None
        amount = amount + (shares_buycell_perdeal*c_close) - brokercost

    if not t1_sells and ((sel_patterns_00 or sel_patterns_01) and c_close >= f_last_fib(target01_ew_rate, fib_range, fibonums)):
        print(f"T1 SELL ENTRY - on {c_date} @ {c_close}")
        t1_sells = c_close
        amount = amount + (shares_buycell_perdeal*c_close) - brokercost

    if t1_sells and (c_low <= f_last_fib(target01_tp_rate, fib_range, fibonums) or c_high >= f_last_fib(target01_sl_rate, fib_range, fibonums)
                     # or c_high-t1_sells<= t1_sells*stoploss_factor
    ):
        print(f"T1 SELL CLOSE - on {c_date} @ {c_close}")
        t1_sells = None
        amount = amount - (shares_buycell_perdeal*c_close) - brokercost

    if not t2_buys and (target02_active and (buy_patterns_00 or buy_patterns_01) and c_close <= f_last_fib(target02_ew_rate, fib_range, fibonums)):
        print(f"T2 BUY ENTRY - on {c_date} @ {c_close}")
        t2_buys = c_close
        amount = amount - (shares_buycell_perdeal*c_close) - brokercost

    if t2_buys and (target02_active and (c_high >= f_last_fib(target02_tp_rate, fib_range, fibonums) or candles[curr].low <= f_last_fib(target02_sl_rate, fib_range, fibonums)
                                         # or t2_buys-c_low<= t2_buys*stoploss_factor
    )):
        print(f"T2 BUY CLOSE - on {c_date} @ {c_close}")
        t2_buys = None
        amount = amount + (shares_buycell_perdeal*c_close) - brokercost

    if not t2_sells and (target02_active and (sel_patterns_00 or sel_patterns_01) and c_close >= f_last_fib(target02_ew_rate, fib_range, fibonums)):
        print(f"T2 SELL ENTRY - on {c_date} @ {c_close}")
        t2_sells = c_close
        amount = amount + (shares_buycell_perdeal*c_close) - brokercost

    if t2_sells and (target02_active and (c_low <= f_last_fib(target02_tp_rate, fib_range, fibonums) or candles[curr].high >= f_last_fib(target02_sl_rate, fib_range, fibonums)
                                          # or c_high-t2_sells<= t2_sells*stoploss_factor
    )):
        print(f"T2 SELL CLOSE - on {c_date} @ {c_close}")
        t2_sells = None
        amount = amount - (shares_buycell_perdeal*c_close) - brokercost

csv_file.close()
print(f"start Rs.{initial_amount} | end Rs.{round(amount,2)} | profit {round(amount-initial_amount,2)} | profit% {round(100*(amount-initial_amount)/initial_amount,2)}%")