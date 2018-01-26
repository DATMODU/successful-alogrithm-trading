# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 11:37:33 2018

@author: cwjang
"""

#%%
os.chdir("./ch07")

#%% 
import pandas as pd
import pymysql 

from localsetting import HOST, USER, PASSWORD


#%% 
db_host = HOST
db_user = USER
db_pass = PASSWORD
db_name = 'securities_master'

conn = pymysql.connect(host=db_host, user=db_user, password=db_pass, 
                       db=db_name, port=9999)

sql = """SELECT dp.price_date, dp.adj_close_price 
FROM symbol AS sym 
INNER JOIN daily_price2 as dp
ON dp.symbol_id = sym.id
WHERE sym.ticker = 'AAPL'
ORDER BY dp.price_date ASC; """

aapl = pd.read_sql_query(sql, con=conn, index_col='price_date')
print(aapl.tail())
