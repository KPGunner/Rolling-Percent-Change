import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt

plt.style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2018, 2, 22)

#Sector Tickers#
#tickers = ['XLV', 'XLU', 'XLE', 'XLB', 'XLI', 'XLP', 'XLRE', 'XLF', 'XLY', 'XLK', 'SPY']

#Defense Tickers#
#tickers = ['BA', 'UTX', 'LMT', 'GD', 'RTN', 'COL', 'LLL', 'TDG', 'HII', 'SPR', 'XAR', 'ITA', 'SPY']
#tickers = ['BA', 'UTX', 'LMT', 'GD', 'RTN', 'COL']
#tickers = ['LLL', 'TDG', 'HII', 'SPR', 'XAR', 'ITA', 'SPY']

df = web.DataReader(tickers, 'yahoo', start, end)

price = df['Adj Close']

pct = price.pct_change(periods=1260, limit=252)*100
print(pct.tail(2))

pct.plot()
plt.title('Rolling Five Year Percent Change')
plt.show()
