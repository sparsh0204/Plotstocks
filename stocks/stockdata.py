from nsepy import get_history
from datetime import date
import pandas as pd


def get_stock_data(symbols):
    df = get_history(symbol=symbols,
                   start=date(2015,1,1),
                   end=date(2016,1,10))
    df['Date'] = pd.to_datetime(df.index)
    #print(df['Date'].dt.strftime('%Y-%m-%d').tolist())
    #df['Date']=df.index
    #print(df['Date'].tolist())
    #print(df['Open'].tolist())
    return df[['Date','Open']]



#dates = pd.to_datetime(pd.Series(['20010101', '20010331']), format = '%Y%m%d')

#print(dates)
#get_stock_data('SBIN')
#print(get_stock_data('SBIN'))