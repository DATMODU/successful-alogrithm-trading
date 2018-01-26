#%%
os.chdir("./ch07")

#%%
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import pymysql

from localsetting import HOST, USER, PASSWORD


#%% Price Data Source를 얻어온다
tickers = ['GOOG', 'AAPL', 'MSFT']

data_source = 'yahoo'
start_date = '2010-01-02'
end_date = '2016-12-31'
panel_data = data.DataReader(tickers, data_source, start_date, end_date)


#%% Adj Close 처리

adj_close = panel_data.ix['Adj Close']
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

adj_close = adj_close.reindex(all_weekdays)
adj_close = adj_close.fillna(method='ffill')



#%% DB에 적재
conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, 
                       db='securities_master', port=9999)

df_ticker = pd.read_sql_query("select id, ticker from symbol;", conn)


for ticker in tickers:
    symbol_id = df_ticker[df_ticker['ticker'] == ticker].id.values[0]
    daily_data = [(int(symbol_id), str(i), float(v)) for i,v in adj_close[ticker].iteritems()]
    
    sql = """insert into daily_price2(symbol_id, price_date, adj_close_price)
    values(%s, %s, %s)"""

    curs = conn.cursor()
    curs.executemany(sql, daily_data)
    conn.commit()
    