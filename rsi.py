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

data1 = pd.DataFrame()
data1 = database['EGIE3.SA']

def rsi_calculator(data, periods):
    
    df = pd.DataFrame()
    df['diff'] =  data.diff()
    df.dropna(inplace=True)
    n = periods
    
    loss = df.mask(data1>0, 0)
    gain = df.mask(data1<0, 0)

    avg_gain = gain.ewm(com=n-1, min_periods=n).mean()
    avg_loss = loss.ewm(com=n-1, min_periods=n).mean()

    rs = abs(avg_gain/avg_loss)

    rsi = 100 - (100/(1+rs))

    df['rsi'] = rsi
    data['rsi'] = df['rsi']
    print(data)
    
rsi_calculator(data1, 14)

