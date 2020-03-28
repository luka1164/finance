import numpy as np 
import pandas as pd
import datetime as dt
from pylab import mpl, plt
import pandas_datareader as web

# SETUP

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'
%matplotlib inline
start = dt.datetime(2019,1,10)
end = dt.datetime(2020,3,28)
tickers = ['EGIE3.SA', 'KLBN11.SA', 'VIVT4.SA', 'WEGE3.SA', 'JBSS3.SA', 'LCAM3.SA', 'VVAR3.SA', 'MGLU3.SA', 'NTCO3.SA', 'PETR4.SA', '^BVSP']

# CREATING A NEW DATAFRAME WITH TICKERS ADJUSTED CLOSE

database = pd.DataFrame()

for ticker in tickers:
    data = web.DataReader(ticker, 'yahoo', start, end)
    database['{}'.format(ticker)] = data['Adj Close']

database.corr()

# CALCULATING THE LOG RETURNS AND CREATING A CORRELATION TABLE

db_ret = pd.DataFrame()
for ticker in tickers:
    db_ret['{}'.format(ticker)] = np.log(database['{}'.format(ticker)]/database['{}'.format(ticker)].shift(1))
    db_ret.dropna(inplace=True)
    
db_ret.corr()

# CREATING A HEATMAP FOR CORRELATION TABLE

fig, ax = plt.subplots()
im = ax.imshow(db_ret.corr(), cmap='hot')

ax.set_xticks(np.arange(len(tickers)))
ax.set_yticks(np.arange(len(tickers)))
ax.set_xticklabels(tickers)
ax.set_yticklabels(tickers)

plt.setp(ax.get_xticklabels(), rotation=90, ha="right", rotation_mode="anchor")

ax.set_title("Log Returns Correlation Map - Nova Futura")
plt.figure(figsize=(100,60))
plt.show()
