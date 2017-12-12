from nsepy import get_history
from datetime import date
import pandas as pd
import datetime


def get_stock_data(symbols, start_date, end_date):

    start = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()

    df = get_history(symbol=symbols,
                   start=start,
                   end=end)
    df['Date'] = pd.to_datetime(df.index)

    return df[['Date','Open']]



#dates = pd.to_datetime(pd.Series(['20010101', '20010331']), format = '%Y%m%d')

#print(dates)
#get_stock_data('SBIN')
#print(get_stock_data('SBIN'))