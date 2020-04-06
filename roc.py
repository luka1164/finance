import numpy as np 
import pandas as pd
import datetime as dt
from pylab import mpl, plt
import pandas_datareader as web

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

start = dt.datetime(2020,1,10)
end = dt.datetime(2020,3,28)
tickers = ['EGIE3.SA']

database = pd.DataFrame()

for ticker in tickers:
    data = web.DataReader(ticker, 'yahoo', start, end)
    database['{}'.format(ticker)] = data['Adj Close']

def roc_calculator(data, periods):
    
    df = pd.DataFrame(index=data.index)
    df['roc'] = ((data/data.shift(periods))-1)*100
    df.dropna(inplace=True)
    data['roc'] = df['roc']
    return data.head()

roc_calculator(db, 1)
