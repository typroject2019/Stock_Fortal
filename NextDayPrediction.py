import tkinter as tk
import json

import urllib.request
import datetime


def predictStock(Name,Size):
    day1 = (datetime.date.today()) - (datetime.timedelta(days=1))
    if day1.weekday() == 5:
        day1 = ((datetime.date.today()) - (datetime.timedelta(days=2)))
        day2 = ((datetime.date.today()) - (datetime.timedelta(days=3)))
        day3 = ((datetime.date.today()) - (datetime.timedelta(days=4)))
        day4 = ((datetime.date.today()) - (datetime.timedelta(days=5)))
        day5 = ((datetime.date.today()) - (datetime.timedelta(days=6)))
        day6 = ((datetime.date.today()) - (datetime.timedelta(days=9)))
        day7 = ((datetime.date.today()) - (datetime.timedelta(days=10)))
        day8 = ((datetime.date.today()) - (datetime.timedelta(days=11)))
        day9 = ((datetime.date.today()) - (datetime.timedelta(days=12)))
        day10 = ((datetime.date.today()) - (datetime.timedelta(days=13)))
    elif day1.weekday() == 4:
        day1 = ((datetime.date.today()) - (datetime.timedelta(days=1)))
        day2 = ((datetime.date.today()) - (datetime.timedelta(days=2)))
        day3 = ((datetime.date.today()) - (datetime.timedelta(days=3)))
        day4 = ((datetime.date.today()) - (datetime.timedelta(days=4)))
        day5 = ((datetime.date.today()) - (datetime.timedelta(days=5)))
        day6 = ((datetime.date.today()) - (datetime.timedelta(days=8)))
        day7 = ((datetime.date.today()) - (datetime.timedelta(days=9)))
        day8 = ((datetime.date.today()) - (datetime.timedelta(days=10)))
        day9 = ((datetime.date.today()) - (datetime.timedelta(days=11)))
        day10 = ((datetime.date.today()) - (datetime.timedelta(days=12)))
    elif day1.weekday() == 3:
        day1 = ((datetime.date.today()) - (datetime.timedelta(days=1)))
        day2 = ((datetime.date.today()) - (datetime.timedelta(days=2)))
        day3 = ((datetime.date.today()) - (datetime.timedelta(days=3)))
        day4 = ((datetime.date.today()) - (datetime.timedelta(days=4)))
        day5 = ((datetime.date.today()) - (datetime.timedelta(days=7)))
        day6 = ((datetime.date.today()) - (datetime.timedelta(days=8)))
        day7 = ((datetime.date.today()) - (datetime.timedelta(days=9)))
        day8 = ((datetime.date.today()) - (datetime.timedelta(days=10)))
        day9 = ((datetime.date.today()) - (datetime.timedelta(days=11)))
        day10 = ((datetime.date.today()) - (datetime.timedelta(days=14)))
    elif day1.weekday() == 2:
        day1 = ((datetime.date.today()) - (datetime.timedelta(days=1)))
        day2 = ((datetime.date.today()) - (datetime.timedelta(days=2)))
        day3 = ((datetime.date.today()) - (datetime.timedelta(days=3)))
        day4 = ((datetime.date.today()) - (datetime.timedelta(days=6)))
        day5 = ((datetime.date.today()) - (datetime.timedelta(days=7)))
        day6 = ((datetime.date.today()) - (datetime.timedelta(days=8)))
        day7 = ((datetime.date.today()) - (datetime.timedelta(days=9)))
        day8 = ((datetime.date.today()) - (datetime.timedelta(days=10)))
        day9 = ((datetime.date.today()) - (datetime.timedelta(days=13)))
        day10 = ((datetime.date.today()) - (datetime.timedelta(days=14)))
    elif day1.weekday() == 1:
        day1 = ((datetime.date.today()) - (datetime.timedelta(days=1)))
        day2 = ((datetime.date.today()) - (datetime.timedelta(days=2)))
        day3 = ((datetime.date.today()) - (datetime.timedelta(days=5)))
        day4 = ((datetime.date.today()) - (datetime.timedelta(days=6)))
        day5 = ((datetime.date.today()) - (datetime.timedelta(days=7)))
        day6 = ((datetime.date.today()) - (datetime.timedelta(days=8)))
        day7 = ((datetime.date.today()) - (datetime.timedelta(days=9)))
        day8 = ((datetime.date.today()) - (datetime.timedelta(days=12)))
        day9 = ((datetime.date.today()) - (datetime.timedelta(days=13)))
        day10 = ((datetime.date.today()) - (datetime.timedelta(days=14)))
    elif day1.weekday() == 0:
        day1 = ((datetime.date.today()) - (datetime.timedelta(days=1)))
        day2 = ((datetime.date.today()) - (datetime.timedelta(days=4)))
        day3 = ((datetime.date.today()) - (datetime.timedelta(days=5)))
        day4 = ((datetime.date.today()) - (datetime.timedelta(days=6)))
        day5 = ((datetime.date.today()) - (datetime.timedelta(days=7)))
        day6 = ((datetime.date.today()) - (datetime.timedelta(days=8)))
        day7 = ((datetime.date.today()) - (datetime.timedelta(days=11)))
        day8 = ((datetime.date.today()) - (datetime.timedelta(days=12)))
        day9 = ((datetime.date.today()) - (datetime.timedelta(days=13)))
        day10 = ((datetime.date.today()) - (datetime.timedelta(days=14)))
    elif day1.weekday() == 6:
        day1 = ((datetime.date.today()) - (datetime.timedelta(days=3)))
        day2 = ((datetime.date.today()) - (datetime.timedelta(days=4)))
        day3 = ((datetime.date.today()) - (datetime.timedelta(days=5)))
        day4 = ((datetime.date.today()) - (datetime.timedelta(days=6)))
        day5 = ((datetime.date.today()) - (datetime.timedelta(days=7)))
        day6 = ((datetime.date.today()) - (datetime.timedelta(days=10)))
        day7 = ((datetime.date.today()) - (datetime.timedelta(days=11)))
        day8 = ((datetime.date.today()) - (datetime.timedelta(days=12)))
        day9 = ((datetime.date.today()) - (datetime.timedelta(days=13)))
        day10 = ((datetime.date.today()) - (datetime.timedelta(days=14)))
    name=Name
    size=Size
    if name == 'TCS.NS':
        j = urllib.request.urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TCS.NS&outputsize=compact&apikey=SNWI14E3V31YMTPY')
        j_obj = json.load(j)

        day1_open = float(j_obj['Time Series (Daily)'][str(day1)]['1. open'])
        day1_high = float(j_obj['Time Series (Daily)'][str(day1)]['2. high'])
        day1_low = float(j_obj['Time Series (Daily)'][str(day1)]['3. low'])
        day1_close = float(j_obj['Time Series (Daily)'][str(day1)]['4. close'])

        day2_open = float(j_obj['Time Series (Daily)'][str(day2)]['1. open'])
        day2_high = float(j_obj['Time Series (Daily)'][str(day2)]['2. high'])
        day2_low = float(j_obj['Time Series (Daily)'][str(day2)]['3. low'])
        day2_close = float(j_obj['Time Series (Daily)'][str(day2)]['4. close'])

        day3_open = float(j_obj['Time Series (Daily)'][str(day3)]['1. open'])
        day3_high = float(j_obj['Time Series (Daily)'][str(day3)]['2. high'])
        day3_low = float(j_obj['Time Series (Daily)'][str(day3)]['3. low'])
        day3_close = float(j_obj['Time Series (Daily)'][str(day3)]['4. close'])

        day4_open = float(j_obj['Time Series (Daily)'][str(day4)]['1. open'])
        day4_high = float(j_obj['Time Series (Daily)'][str(day4)]['2. high'])
        day4_low = float(j_obj['Time Series (Daily)'][str(day4)]['3. low'])
        day4_close = float(j_obj['Time Series (Daily)'][str(day4)]['4. close'])

        day5_open = float(j_obj['Time Series (Daily)'][str(day5)]['1. open'])
        day5_high = float(j_obj['Time Series (Daily)'][str(day5)]['2. high'])
        day5_low = float(j_obj['Time Series (Daily)'][str(day5)]['3. low'])
        day5_close = float(j_obj['Time Series (Daily)'][str(day5)]['4. close'])

        day6_open = float(j_obj['Time Series (Daily)'][str(day6)]['1. open'])
        day6_high = float(j_obj['Time Series (Daily)'][str(day6)]['2. high'])
        day6_low = float(j_obj['Time Series (Daily)'][str(day6)]['3. low'])
        day6_close = float(j_obj['Time Series (Daily)'][str(day6)]['4. close'])

        day7_open = float(j_obj['Time Series (Daily)'][str(day7)]['1. open'])
        day7_high = float(j_obj['Time Series (Daily)'][str(day7)]['2. high'])
        day7_low = float(j_obj['Time Series (Daily)'][str(day7)]['3. low'])
        day7_close = float(j_obj['Time Series (Daily)'][str(day7)]['4. close'])

        day8_open = float(j_obj['Time Series (Daily)'][str(day8)]['1. open'])
        day8_high = float(j_obj['Time Series (Daily)'][str(day8)]['2. high'])
        day8_low = float(j_obj['Time Series (Daily)'][str(day8)]['3. low'])
        day8_close = float(j_obj['Time Series (Daily)'][str(day8)]['4. close'])

        day9_open = float(j_obj['Time Series (Daily)'][str(day9)]['1. open'])
        day9_high = float(j_obj['Time Series (Daily)'][str(day9)]['2. high'])
        day9_low = float(j_obj['Time Series (Daily)'][str(day9)]['3. low'])
        day9_close = float(j_obj['Time Series (Daily)'][str(day9)]['4. close'])

        day10_open = float(j_obj['Time Series (Daily)'][str(day10)]['1. open'])
        day10_high = float(j_obj['Time Series (Daily)'][str(day10)]['2. high'])
        day10_low = float(j_obj['Time Series (Daily)'][str(day10)]['3. low'])
        day10_close = float(j_obj['Time Series (Daily)'][str(day10)]['4. close'])
        if size == 5:
            d5open_avg = ((day1_open + day2_open + day3_open + day4_open + day5_open) / 5)
            d5close_avg = (day1_close + day2_close + day3_close + day4_close + day5_close) / 5
            d5high_avg = (day1_high + day2_high + day3_high + day4_high + day5_high) / 5
            d5low_avg = (day1_low + day2_low + day3_low + day4_low + day5_low) / 5
            d5ochl_avg = (d5open_avg + d5close_avg + d5low_avg + d5high_avg) / 4
            target = d5high_avg
            stoploss = d5low_avg
            avg_tag_stop = (target + stoploss) / 2
            if (d5ochl_avg <= avg_tag_stop):
                tk.Label(root,text='Indication: Sell', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4,column=1)
                print('Indication:Sell')
            else:
                print('Indication:Buy')
                tk.Label(root, text='Indication: Buy', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4, column=1)
            print(target, 'target of the day')
            print(stoploss, 'stoploss of the day')
            tk.Label(root, text='Target of the day : '+str(target), bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=6, column=1)
            tk.Label(root, text='Stoploss of the day : '+str(stoploss), bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=7, column=1)
        elif (size == 10):
            d10open_avg = (day1_open + day2_open + day3_open + day4_open + day5_open + day6_open + day7_open + day8_open + day9_open + day10_open) / 10
            d10close_avg = (day1_close + day2_close + day3_close + day4_close + day5_close + day6_close + day7_close + day8_close + day9_close + day10_close) / 10
            d10high_avg = (day1_high + day2_high + day3_high + day4_high + day5_high + day6_high + day7_high + day8_high + day9_high + day10_high) / 10
            d10low_avg = (day1_low + day2_low + day3_low + day4_low + day5_low + day6_low + day7_low + day8_low + day9_low + day10_low) / 10
            d10ochl_avg = (d10open_avg + d10close_avg + d10low_avg + d10high_avg) / 4
            target = d10high_avg
            stoploss = d10low_avg
            avg_tag_stop = (target + stoploss) / 2
            if (d10ochl_avg <= avg_tag_stop):
                print('Indication:Sell')
                tk.Label(root, text='Indication: Sell', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4, column=1)
            else:
                print('Indication:Buy')
                tk.Label(root, text='Indication: Buy', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4, column=1)
            print(target, 'target of the day')
            print(stoploss, 'stoploss of the day')
            tk.Label(root, text='Target of the day : ' + str(target), bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=6, column=1)
            tk.Label(root, text='Stoploss of the day : ' + str(stoploss), bg='light sky blue',font='-weight bold', justify='center', padx='5', pady='5').grid(row=7, column=1)
    elif (name == 'HDFCBANK.NS'):
        j = urllib.request.urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=HDFCBANK.NS&outputsize=compact&apikey=SNWI14E3V31YMTPY')
        j_obj = json.load(j)

        day1_open = float(j_obj['Time Series (Daily)'][str(day1)]['1. open'])
        day1_high = float(j_obj['Time Series (Daily)'][str(day1)]['2. high'])
        day1_low = float(j_obj['Time Series (Daily)'][str(day1)]['3. low'])
        day1_close = float(j_obj['Time Series (Daily)'][str(day1)]['4. close'])

        day2_open = float(j_obj['Time Series (Daily)'][str(day2)]['1. open'])
        day2_high = float(j_obj['Time Series (Daily)'][str(day2)]['2. high'])
        day2_low = float(j_obj['Time Series (Daily)'][str(day2)]['3. low'])
        day2_close = float(j_obj['Time Series (Daily)'][str(day2)]['4. close'])

        day3_open = float(j_obj['Time Series (Daily)'][str(day3)]['1. open'])
        day3_high = float(j_obj['Time Series (Daily)'][str(day3)]['2. high'])
        day3_low = float(j_obj['Time Series (Daily)'][str(day3)]['3. low'])
        day3_close = float(j_obj['Time Series (Daily)'][str(day3)]['4. close'])

        day4_open = float(j_obj['Time Series (Daily)'][str(day4)]['1. open'])
        day4_high = float(j_obj['Time Series (Daily)'][str(day4)]['2. high'])
        day4_low = float(j_obj['Time Series (Daily)'][str(day4)]['3. low'])
        day4_close = float(j_obj['Time Series (Daily)'][str(day4)]['4. close'])

        day5_open = float(j_obj['Time Series (Daily)'][str(day5)]['1. open'])
        day5_high = float(j_obj['Time Series (Daily)'][str(day5)]['2. high'])
        day5_low = float(j_obj['Time Series (Daily)'][str(day5)]['3. low'])
        day5_close = float(j_obj['Time Series (Daily)'][str(day5)]['4. close'])

        day6_open = float(j_obj['Time Series (Daily)'][str(day6)]['1. open'])
        day6_high = float(j_obj['Time Series (Daily)'][str(day6)]['2. high'])
        day6_low = float(j_obj['Time Series (Daily)'][str(day6)]['3. low'])
        day6_close = float(j_obj['Time Series (Daily)'][str(day6)]['4. close'])

        day7_open = float(j_obj['Time Series (Daily)'][str(day7)]['1. open'])
        day7_high = float(j_obj['Time Series (Daily)'][str(day7)]['2. high'])
        day7_low = float(j_obj['Time Series (Daily)'][str(day7)]['3. low'])
        day7_close = float(j_obj['Time Series (Daily)'][str(day7)]['4. close'])

        day8_open = float(j_obj['Time Series (Daily)'][str(day8)]['1. open'])
        day8_high = float(j_obj['Time Series (Daily)'][str(day8)]['2. high'])
        day8_low = float(j_obj['Time Series (Daily)'][str(day8)]['3. low'])
        day8_close = float(j_obj['Time Series (Daily)'][str(day8)]['4. close'])

        day9_open = float(j_obj['Time Series (Daily)'][str(day9)]['1. open'])
        day9_high = float(j_obj['Time Series (Daily)'][str(day9)]['2. high'])
        day9_low = float(j_obj['Time Series (Daily)'][str(day9)]['3. low'])
        day9_close = float(j_obj['Time Series (Daily)'][str(day9)]['4. close'])

        day10_open = float(j_obj['Time Series (Daily)'][str(day10)]['1. open'])
        day10_high = float(j_obj['Time Series (Daily)'][str(day10)]['2. high'])
        day10_low = float(j_obj['Time Series (Daily)'][str(day10)]['3. low'])
        day10_close = float(j_obj['Time Series (Daily)'][str(day10)]['4. close'])
        if (size == 5):
            d5open_avg = (day1_open + day2_open + day3_open + day4_open + day5_open) / 5
            d5close_avg = (day1_close + day2_close + day3_close + day4_close + day5_close) / 5
            d5high_avg = (day1_high + day2_high + day3_high + day4_high + day5_high) / 5
            d5low_avg = (day1_low + day2_low + day3_low + day4_low + day5_low) / 5
            d5ochl_avg = (d5open_avg + d5close_avg + d5low_avg + d5high_avg) / 4
            target = d5high_avg
            stoploss = d5low_avg
            avg_tag_stop = (target + stoploss) / 2
            if (d5ochl_avg <= avg_tag_stop):
                print('Indication:Sell')
                tk.Label(root, text='Indication: Sell', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4, column=1)
            else:
                print('Indication:Buy')
                tk.Label(root, text='Indication: Buy', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4, column=1)
            print(target, 'target of the day')
            print(stoploss, 'stoploss of the day')
            tk.Label(root, text='Target of the day : ' + str(target), bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=6, column=1)
            tk.Label(root, text='Stoploss of the day : ' + str(stoploss), bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=7, column=1)
        elif (size == 10):
            d10open_avg = (day1_open + day2_open + day3_open + day4_open + day5_open + day6_open + day7_open + day8_open + day9_open + day10_open) / 10
            d10close_avg = (day1_close + day2_close + day3_close + day4_close + day5_close + day6_close + day7_close + day8_close + day9_close + day10_close) / 10
            d10high_avg = (day1_high + day2_high + day3_high + day4_high + day5_high + day6_high + day7_high + day8_high + day9_high + day10_high) / 10
            d10low_avg = (day1_low + day2_low + day3_low + day4_low + day5_low + day6_low + day7_low + day8_low + day9_low + day10_low) / 10
            d10ochl_avg = (d10open_avg + d10close_avg + d10low_avg + d10high_avg) / 4
            target = d10high_avg
            stoploss = d10low_avg
            avg_tag_stop = (target + stoploss) / 2
            if (d10ochl_avg <= avg_tag_stop):
                print('Indication:Sell')
                tk.Label(root, text='Indication: Sell', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4, column=1)
            else:
                print('Indication:Buy')
                tk.Label(root, text='Indication: Buy', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4, column=1)
            print(target, 'target of the day')
            print(stoploss, 'stoploss of the day')
            tk.Label(root, text='Target of the day : ' + str(target), bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=6, column=1)
            tk.Label(root, text='Stoploss of the day : ' + str(stoploss), bg='light sky blue',font='-weight bold', justify='center', padx='5', pady='5').grid(row=7, column=1)
    elif (name == 'ONGC.NS'):
        j = urllib.request.urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=ONGC.NS&outputsize=compact&apikey=SNWI14E3V31YMTPY')
        j_obj = json.load(j)

        day1_open = float(j_obj['Time Series (Daily)'][str(day1)]['1. open'])
        day1_high = float(j_obj['Time Series (Daily)'][str(day1)]['2. high'])
        day1_low = float(j_obj['Time Series (Daily)'][str(day1)]['3. low'])
        day1_close = float(j_obj['Time Series (Daily)'][str(day1)]['4. close'])

        day2_open = float(j_obj['Time Series (Daily)'][str(day2)]['1. open'])
        day2_high = float(j_obj['Time Series (Daily)'][str(day2)]['2. high'])
        day2_low = float(j_obj['Time Series (Daily)'][str(day2)]['3. low'])
        day2_close = float(j_obj['Time Series (Daily)'][str(day2)]['4. close'])

        day3_open = float(j_obj['Time Series (Daily)'][str(day3)]['1. open'])
        day3_high = float(j_obj['Time Series (Daily)'][str(day3)]['2. high'])
        day3_low = float(j_obj['Time Series (Daily)'][str(day3)]['3. low'])
        day3_close = float(j_obj['Time Series (Daily)'][str(day3)]['4. close'])

        day4_open = float(j_obj['Time Series (Daily)'][str(day4)]['1. open'])
        day4_high = float(j_obj['Time Series (Daily)'][str(day4)]['2. high'])
        day4_low = float(j_obj['Time Series (Daily)'][str(day4)]['3. low'])
        day4_close = float(j_obj['Time Series (Daily)'][str(day4)]['4. close'])

        day5_open = float(j_obj['Time Series (Daily)'][str(day5)]['1. open'])
        day5_high = float(j_obj['Time Series (Daily)'][str(day5)]['2. high'])
        day5_low = float(j_obj['Time Series (Daily)'][str(day5)]['3. low'])
        day5_close = float(j_obj['Time Series (Daily)'][str(day5)]['4. close'])

        day6_open = float(j_obj['Time Series (Daily)'][str(day6)]['1. open'])
        day6_high = float(j_obj['Time Series (Daily)'][str(day6)]['2. high'])
        day6_low = float(j_obj['Time Series (Daily)'][str(day6)]['3. low'])
        day6_close = float(j_obj['Time Series (Daily)'][str(day6)]['4. close'])

        day7_open = float(j_obj['Time Series (Daily)'][str(day7)]['1. open'])
        day7_high = float(j_obj['Time Series (Daily)'][str(day7)]['2. high'])
        day7_low = float(j_obj['Time Series (Daily)'][str(day7)]['3. low'])
        day7_close = float(j_obj['Time Series (Daily)'][str(day7)]['4. close'])

        day8_open = float(j_obj['Time Series (Daily)'][str(day8)]['1. open'])
        day8_high = float(j_obj['Time Series (Daily)'][str(day8)]['2. high'])
        day8_low = float(j_obj['Time Series (Daily)'][str(day8)]['3. low'])
        day8_close = float(j_obj['Time Series (Daily)'][str(day8)]['4. close'])

        day9_open = float(j_obj['Time Series (Daily)'][str(day9)]['1. open'])
        day9_high = float(j_obj['Time Series (Daily)'][str(day9)]['2. high'])
        day9_low = float(j_obj['Time Series (Daily)'][str(day9)]['3. low'])
        day9_close = float(j_obj['Time Series (Daily)'][str(day9)]['4. close'])

        day10_open = float(j_obj['Time Series (Daily)'][str(day10)]['1. open'])
        day10_high = float(j_obj['Time Series (Daily)'][str(day10)]['2. high'])
        day10_low = float(j_obj['Time Series (Daily)'][str(day10)]['3. low'])
        day10_close = float(j_obj['Time Series (Daily)'][str(day10)]['4. close'])
        if (size == 5):
            d5open_avg = (day1_open + day2_open + day3_open + day4_open + day5_open) / 5
            d5close_avg = (day1_close + day2_close + day3_close + day4_close + day5_close) / 5
            d5high_avg = (day1_high + day2_high + day3_high + day4_high + day5_high) / 5
            d5low_avg = (day1_low + day2_low + day3_low + day4_low + day5_low) / 5
            d5ochl_avg = (d5open_avg + d5close_avg + d5low_avg + d5high_avg) / 4
            target = d5high_avg
            stoploss = d5low_avg
            avg_tag_stop = (target + stoploss) / 2
            if (d5ochl_avg <= avg_tag_stop):
                print('Indication:Sell')
                tk.Label(root, text='Indication: Sell', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4, column=1)
            else:
                print('Indication:Buy')
                tk.Label(root, text='Indication: Buy', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4, column=1)
            print(target, 'target of the day')
            print(stoploss, 'stoploss of the day')
            tk.Label(root, text='Target of the day : ' + str(target), bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=6, column=1)
            tk.Label(root, text='Stoploss of the day : ' + str(stoploss), bg='light sky blue',font='-weight bold', justify='center', padx='5', pady='5').grid(row=7, column=1)
        elif (size == 10):
            d10open_avg = (day1_open + day2_open + day3_open + day4_open + day5_open + day6_open + day7_open + day8_open + day9_open + day10_open) / 10
            d10close_avg = (day1_close + day2_close + day3_close + day4_close + day5_close + day6_close + day7_close + day8_close + day9_close + day10_close) / 10
            d10high_avg = (day1_high + day2_high + day3_high + day4_high + day5_high + day6_high + day7_high + day8_high + day9_high + day10_high) / 10
            d10low_avg = (day1_low + day2_low + day3_low + day4_low + day5_low + day6_low + day7_low + day8_low + day9_low + day10_low) / 10
            d10ochl_avg = (d10open_avg + d10close_avg + d10low_avg + d10high_avg) / 4
            target = d10high_avg
            stoploss = d10low_avg
            avg_tag_stop = (target + stoploss) / 2
            if (d10ochl_avg <= avg_tag_stop):
                print('Indication:Sell')
                tk.Label(root, text='Indication: Sell', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4, column=1)
            else:
                print('Indication:Buy')
                tk.Label(root, text='Indication: Buy', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4, column=1)
            print(target, 'target of the day')
            print(stoploss, 'stoploss of the day')
            tk.Label(root, text='Target of the day : ' + str(target), bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=6, column=1)
            tk.Label(root, text='Stoploss of the day : ' + str(stoploss), bg='light sky blue',font='-weight bold', justify='center', padx='5', pady='5').grid(row=7, column=1)
    elif (name == 'ASIANPAINT.NS'):
        j = urllib.request.urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=ASIANPAINT.NS&outputsize=compact&apikey=SNWI14E3V31YMTPY')
        j_obj = json.load(j)

        day1_open = float(j_obj['Time Series (Daily)'][str(day1)]['1. open'])
        day1_high = float(j_obj['Time Series (Daily)'][str(day1)]['2. high'])
        day1_low = float(j_obj['Time Series (Daily)'][str(day1)]['3. low'])
        day1_close = float(j_obj['Time Series (Daily)'][str(day1)]['4. close'])

        day2_open = float(j_obj['Time Series (Daily)'][str(day2)]['1. open'])
        day2_high = float(j_obj['Time Series (Daily)'][str(day2)]['2. high'])
        day2_low = float(j_obj['Time Series (Daily)'][str(day2)]['3. low'])
        day2_close = float(j_obj['Time Series (Daily)'][str(day2)]['4. close'])

        day3_open = float(j_obj['Time Series (Daily)'][str(day3)]['1. open'])
        day3_high = float(j_obj['Time Series (Daily)'][str(day3)]['2. high'])
        day3_low = float(j_obj['Time Series (Daily)'][str(day3)]['3. low'])
        day3_close = float(j_obj['Time Series (Daily)'][str(day3)]['4. close'])

        day4_open = float(j_obj['Time Series (Daily)'][str(day4)]['1. open'])
        day4_high = float(j_obj['Time Series (Daily)'][str(day4)]['2. high'])
        day4_low = float(j_obj['Time Series (Daily)'][str(day4)]['3. low'])
        day4_close = float(j_obj['Time Series (Daily)'][str(day4)]['4. close'])

        day5_open = float(j_obj['Time Series (Daily)'][str(day5)]['1. open'])
        day5_high = float(j_obj['Time Series (Daily)'][str(day5)]['2. high'])
        day5_low = float(j_obj['Time Series (Daily)'][str(day5)]['3. low'])
        day5_close = float(j_obj['Time Series (Daily)'][str(day5)]['4. close'])

        day6_open = float(j_obj['Time Series (Daily)'][str(day6)]['1. open'])
        day6_high = float(j_obj['Time Series (Daily)'][str(day6)]['2. high'])
        day6_low = float(j_obj['Time Series (Daily)'][str(day6)]['3. low'])
        day6_close = float(j_obj['Time Series (Daily)'][str(day6)]['4. close'])

        day7_open = float(j_obj['Time Series (Daily)'][str(day7)]['1. open'])
        day7_high = float(j_obj['Time Series (Daily)'][str(day7)]['2. high'])
        day7_low = float(j_obj['Time Series (Daily)'][str(day7)]['3. low'])
        day7_close = float(j_obj['Time Series (Daily)'][str(day7)]['4. close'])

        day8_open = float(j_obj['Time Series (Daily)'][str(day8)]['1. open'])
        day8_high = float(j_obj['Time Series (Daily)'][str(day8)]['2. high'])
        day8_low = float(j_obj['Time Series (Daily)'][str(day8)]['3. low'])
        day8_close = float(j_obj['Time Series (Daily)'][str(day8)]['4. close'])

        day9_open = float(j_obj['Time Series (Daily)'][str(day9)]['1. open'])
        day9_high = float(j_obj['Time Series (Daily)'][str(day9)]['2. high'])
        day9_low = float(j_obj['Time Series (Daily)'][str(day9)]['3. low'])
        day9_close = float(j_obj['Time Series (Daily)'][str(day9)]['4. close'])

        day10_open = float(j_obj['Time Series (Daily)'][str(day10)]['1. open'])
        day10_high = float(j_obj['Time Series (Daily)'][str(day10)]['2. high'])
        day10_low = float(j_obj['Time Series (Daily)'][str(day10)]['3. low'])
        day10_close = float(j_obj['Time Series (Daily)'][str(day10)]['4. close'])
        if (size == 5):
            d5open_avg = (day1_open + day2_open + day3_open + day4_open + day5_open) / 5
            d5close_avg = (day1_close + day2_close + day3_close + day4_close + day5_close) / 5
            d5high_avg = (day1_high + day2_high + day3_high + day4_high + day5_high) / 5
            d5low_avg = (day1_low + day2_low + day3_low + day4_low + day5_low) / 5
            d5ochl_avg = (d5open_avg + d5close_avg + d5low_avg + d5high_avg) / 4
            target = d5high_avg
            stoploss = d5low_avg
            avg_tag_stop = (target + stoploss) / 2
            if (d5ochl_avg <= avg_tag_stop):
                print('Indication:Sell')
                tk.Label(root, text='Indication: Sell', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4, column=1)
            else:
                print('Indication:Buy')
                tk.Label(root, text='Indication: Buy', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4, column=1)
            print(target, 'target of the day')
            print(stoploss, 'stoploss of the day')
            tk.Label(root, text='Target of the day : ' + str(target), bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=6, column=1)
            tk.Label(root, text='Stoploss of the day : ' + str(stoploss), bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=7, column=1)
        elif (size == 10):
            d10open_avg = (day1_open + day2_open + day3_open + day4_open + day5_open + day6_open + day7_open + day8_open + day9_open + day10_open) / 10
            d10close_avg = (day1_close + day2_close + day3_close + day4_close + day5_close + day6_close + day7_close + day8_close + day9_close + day10_close) / 10
            d10high_avg = (day1_high + day2_high + day3_high + day4_high + day5_high + day6_high + day7_high + day8_high + day9_high + day10_high) / 10
            d10low_avg = (day1_low + day2_low + day3_low + day4_low + day5_low + day6_low + day7_low + day8_low + day9_low + day10_low) / 10
            d10ochl_avg = (d10open_avg + d10close_avg + d10low_avg + d10high_avg) / 4
            target = d10high_avg
            stoploss = d10low_avg
            avg_tag_stop = (target + stoploss) / 2
            if (d10ochl_avg <= avg_tag_stop):
                print('Indication:Sell')
                tk.Label(root, text='Indication: Sell', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4, column=1)
            else:
                print('Indication:Buy')
                tk.Label(root, text='Indication: Buy', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4, column=1)
            print(target, 'target of the day')
            print(stoploss, 'stoploss of the day')
            tk.Label(root, text='Target of the day : ' + str(target), bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=6, column=1)
            tk.Label(root, text='Stoploss of the day : ' + str(stoploss), bg='light sky blue',font='-weight bold', justify='center', padx='5', pady='5').grid(row=7, column=1)
    elif (name == 'MARUTI.NS'):
        j = urllib.request.urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MARUTI.NS&outputsize=compact&apikey=SNWI14E3V31YMTPY')
        j_obj = json.load(j)

        day1_open = float(j_obj['Time Series (Daily)'][str(day1)]['1. open'])
        day1_high = float(j_obj['Time Series (Daily)'][str(day1)]['2. high'])
        day1_low = float(j_obj['Time Series (Daily)'][str(day1)]['3. low'])
        day1_close = float(j_obj['Time Series (Daily)'][str(day1)]['4. close'])

        day2_open = float(j_obj['Time Series (Daily)'][str(day2)]['1. open'])
        day2_high = float(j_obj['Time Series (Daily)'][str(day2)]['2. high'])
        day2_low = float(j_obj['Time Series (Daily)'][str(day2)]['3. low'])
        day2_close = float(j_obj['Time Series (Daily)'][str(day2)]['4. close'])

        day3_open = float(j_obj['Time Series (Daily)'][str(day3)]['1. open'])
        day3_high = float(j_obj['Time Series (Daily)'][str(day3)]['2. high'])
        day3_low = float(j_obj['Time Series (Daily)'][str(day3)]['3. low'])
        day3_close = float(j_obj['Time Series (Daily)'][str(day3)]['4. close'])

        day4_open = float(j_obj['Time Series (Daily)'][str(day4)]['1. open'])
        day4_high = float(j_obj['Time Series (Daily)'][str(day4)]['2. high'])
        day4_low = float(j_obj['Time Series (Daily)'][str(day4)]['3. low'])
        day4_close = float(j_obj['Time Series (Daily)'][str(day4)]['4. close'])

        day5_open = float(j_obj['Time Series (Daily)'][str(day5)]['1. open'])
        day5_high = float(j_obj['Time Series (Daily)'][str(day5)]['2. high'])
        day5_low = float(j_obj['Time Series (Daily)'][str(day5)]['3. low'])
        day5_close = float(j_obj['Time Series (Daily)'][str(day5)]['4. close'])

        day6_open = float(j_obj['Time Series (Daily)'][str(day6)]['1. open'])
        day6_high = float(j_obj['Time Series (Daily)'][str(day6)]['2. high'])
        day6_low = float(j_obj['Time Series (Daily)'][str(day6)]['3. low'])
        day6_close = float(j_obj['Time Series (Daily)'][str(day6)]['4. close'])

        day7_open = float(j_obj['Time Series (Daily)'][str(day7)]['1. open'])
        day7_high = float(j_obj['Time Series (Daily)'][str(day7)]['2. high'])
        day7_low = float(j_obj['Time Series (Daily)'][str(day7)]['3. low'])
        day7_close = float(j_obj['Time Series (Daily)'][str(day7)]['4. close'])

        day8_open = float(j_obj['Time Series (Daily)'][str(day8)]['1. open'])
        day8_high = float(j_obj['Time Series (Daily)'][str(day8)]['2. high'])
        day8_low = float(j_obj['Time Series (Daily)'][str(day8)]['3. low'])
        day8_close = float(j_obj['Time Series (Daily)'][str(day8)]['4. close'])

        day9_open = float(j_obj['Time Series (Daily)'][str(day9)]['1. open'])
        day9_high = float(j_obj['Time Series (Daily)'][str(day9)]['2. high'])
        day9_low = float(j_obj['Time Series (Daily)'][str(day9)]['3. low'])
        day9_close = float(j_obj['Time Series (Daily)'][str(day9)]['4. close'])

        day10_open = float(j_obj['Time Series (Daily)'][str(day10)]['1. open'])
        day10_high = float(j_obj['Time Series (Daily)'][str(day10)]['2. high'])
        day10_low = float(j_obj['Time Series (Daily)'][str(day10)]['3. low'])
        day10_close = float(j_obj['Time Series (Daily)'][str(day10)]['4. close'])
        if (size == 5):
            d5open_avg = (day1_open + day2_open + day3_open + day4_open + day5_open) / 5
            d5close_avg = (day1_close + day2_close + day3_close + day4_close + day5_close) / 5
            d5high_avg = (day1_high + day2_high + day3_high + day4_high + day5_high) / 5
            d5low_avg = (day1_low + day2_low + day3_low + day4_low + day5_low) / 5
            d5ochl_avg = (d5open_avg + d5close_avg + d5low_avg + d5high_avg) / 4
            target = d5high_avg
            stoploss = d5low_avg
            avg_tag_stop = (target + stoploss) / 2
            if (d5ochl_avg <= avg_tag_stop):
                print('Indication:Sell')
                tk.Label(root, text='Indication: Sell', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4, column=1)
            else:
                print('Indication:Buy')
                tk.Label(root, text='Indication: Buy', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4, column=1)
            print(target, 'target of the day')
            print(stoploss, 'stoploss of the day')
            tk.Label(root, text='Target of the day : ' + str(target), bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=6, column=1)
            tk.Label(root, text='Stoploss of the day : ' + str(stoploss), bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=7, column=1)
        elif (size == 10):
            d10open_avg = (day1_open + day2_open + day3_open + day4_open + day5_open + day6_open + day7_open + day8_open + day9_open + day10_open) / 10
            d10close_avg = (day1_close + day2_close + day3_close + day4_close + day5_close + day6_close + day7_close + day8_close + day9_close + day10_close) / 10
            d10high_avg = (day1_high + day2_high + day3_high + day4_high + day5_high + day6_high + day7_high + day8_high + day9_high + day10_high) / 10
            d10low_avg = (day1_low + day2_low + day3_low + day4_low + day5_low + day6_low + day7_low + day8_low + day9_low + day10_low) / 10
            d10ochl_avg = (d10open_avg + d10close_avg + d10low_avg + d10high_avg) / 4
            target = d10high_avg
            stoploss = d10low_avg
            avg_tag_stop = (target + stoploss) / 2
            if (d10ochl_avg <= avg_tag_stop):
                print('Indication:Sell')
                tk.Label(root, text='Indication: Sell', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4, column=1)
            else:
                print('Indication:Buy')
                tk.Label(root, text='Indication: Buy', bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=4, column=1)
            print(target, 'target of the day')
            print(stoploss, 'stoploss of the day')
            tk.Label(root, text='Target of the day : ' + str(target), bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=6, column=1)
            tk.Label(root, text='Stoploss of the day : ' + str(stoploss), bg='light sky blue', font='-weight bold', justify='center', padx='5', pady='5').grid(row=7, column=1)


root=tk.Tk()
root.configure(background='light sky blue')
root.title('Stock Fortal Application')
root.geometry("900x600")

l1=tk.Label(root, text="Select the company : ", bg='light sky blue', font='-weight bold', justify='center', padx='20', pady='20').grid(row=1,column=1)
l2=tk.Label(root, text='Select the input size : ', bg='light sky blue' , font='-weight bold').grid(row=2, column=1)




tkvar=tk.StringVar(root)
choices={'TCS.NS', 'HDFCBANK.NS', 'ONGC.NS', 'ASIANPAINT.NS', 'MARUTI.NS'}
tkvar.set('MARUTI.NS')
popupMenu=tk.OptionMenu(root,tkvar,*choices,)
popupMenu.configure(bg='light cyan')
popupMenu.grid(row=1,column=2)


tkvar1=tk.StringVar(root)
choices1={'5', '10'}
tkvar1.set('5')
popupMenu1=tk.OptionMenu(root,tkvar1, *choices1)
popupMenu1.configure(bg='light cyan')
popupMenu1.grid(row=2,column=2)


def insert():
    Cname=tkvar.get()
    Size=int(tkvar1.get())
    predictStock(Cname,Size)


submit = tk.Button(root, text="Get Prediction", fg="Black", bg="azure", command=insert, font='-weight bold')
submit.grid(row=3,column=1)

root.mainloop()