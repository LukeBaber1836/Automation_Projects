import requests
import time
from datetime import datetime

ticker_smbl = input("Enter ticker symbol: ")
from_date = input("Enter start date of stock info: yyyy/mm/dd ")
to_date = input("Enter end date of stock info: yyyy/mm/dd ")

date_f = datetime.strptime(from_date, "%Y/%m/%d")
date_t = datetime.strptime(to_date, "%Y/%m/%d")

from_date_sec = int(time.mktime(date_f.timetuple()))
to_date_sec = int(time.mktime(date_t.timetuple()))

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker_smbl}?period1={from_date_sec}&period2={to_date_sec}&interval=1d&events=history&includeAdjustedClose=true"
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}

data = requests.get(url, headers=headers).content

#download binary files and write to .csv
data_file = open ("stock_data.csv", "w")
data_file.write(ticker_smbl + "\n")
with open ("stock_data.csv", "wb") as file:
    file.write(data)

