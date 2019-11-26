import os
import csv
import requests
import json
import datetime
from pytz import timezone
import time

def btc_price():
    global symbol, percent, price_now, volume
    response = requests.get("https://www.bitmex.com/api/v1/instrument")
    data = json.loads(response.text)
    symbol = data[88]["symbol"]
    percent = data[88]["lastChangePcnt"]
    price_now = data[88]["midPrice"]
    volume = data[88]["volume"]
    print(percent)
    print(price_now)
    print(volume)

def now():
    global month, day, hour, minute
    now_time = datetime.datetime.now(timezone('Asia/Tokyo'))
    month = str(now_time.month)
    day = str(now_time.day)
    hour = str(now_time.hour)
    minute = str(now_time.minute)

def write_csv1():
    with open("XBTUSD" + month + day + ".csv", "a") as csvFile:
        writer = csv.writer(csvFile)
        header = ["Hour", "Minute","Price_now", "Percentage", "Volume"]
        writer.writerow(header)
        writer.writerow([hour, minute,price_now, percent, volume])
    csvFile.close()

def write_csv2():
    with open("XBTUSD" + month + day + ".csv", "a") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow([hour, minute,price_now, percent, volume])
    csvFile.close()


loop_time = 1
while True:
    now()
    start_day = int(day)
    start_h = 3
    start_m = 13
    if int(hour) == start_h and int(minute) == start_m:
        while True:
            now()
            try:
                btc_price()
                if loop_time == 1 or looping_day != int(day):
                    write_csv1()
                    print("CSVファイルの作成に成功\n")
                    loop_time = loop_time + 1
                    looping_day = int(day)
                    time.sleep(60)
                else:
                    write_csv2()
                    print("ループ回数：" + str(loop_time) + "  CSV書き込みOK\n")
                    loop_time = loop_time + 1
                    looping_day = int(day)
                    time.sleep(60)
            except:
                print("try: エラーだよ")
                loop_time = loop_time + 1
    else:
        pass