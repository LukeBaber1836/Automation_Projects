from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
import datetime


c = CurrencyRates()
c.get_rates('USD')

b = BtcConverter()
start_date = datetime.datetime(2016, 5, 18, 19, 39, 36, 815417)
end_date = datetime.datetime(2016, 5, 23, 19, 39, 36, 815417)
print(b.get_previous_price_list('USD', start_date, end_date))


# print(b.get_latest_price('USD'))

