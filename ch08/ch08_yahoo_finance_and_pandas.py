# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 12:38:13 2018

@author: cwjang
"""

#%%
import datetime
from pandas_datareader import data

# 기존 코드(Python2 Pandas)
#spy = web.DataReader("SPY", "yahoo", 
#                     datetime.datetime(2007, 1, 1), 
#                     datetime.datetime(2015, 6, 15))

#panel_data = data.DataReader(tickers, data_source, start_date, end_date)
#
#
##%% Adj Close 처리
#
#adj_close = panel_data.ix['Adj Close']
#all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
#
#adj_close = adj_close.reindex(all_weekdays)
#adj_close = adj_close.fillna(method='ffill')


# Python3 Pandas
spy = data.DataReader("SPY", "yahoo",  datetime.datetime(2007, 1, 1), datetime.datetime(2015, 6, 15))
