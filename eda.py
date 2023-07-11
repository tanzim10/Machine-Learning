# -*- coding: utf-8 -*-
"""EDA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uAbxRuBsUlAINLUAJKEHPjf8GVPTcqLb

##Exploritary Data Analysis
"""

import pandas as pd
import yfinance as yf
import numpy as np
import pandas_datareader as web
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
pd.set_option('display.max_columns',100)

symbol = 'MSFT'
    start_date = '2012-01-01'
    end_date = '2021-12-17'

    # Get the stock quote
    df = yf.download(symbol, start=start_date, end=end_date)
    df



"""## Data  Understanding"""

df.head(20)

df.columns

df.dtypes

df.describe()

"""##Data Preparations"""

df = df[['Open', 'High', 'Low', 'Close', 'Volume',
       ]].copy()
df.head()

#df.drop(['split cofficient', axis = 1]). Dropping single column

df.shape

#Rename  our columns
df.rename(columns = {'adjusted close':'Adjusted_Close',
                     'open':'Open',
                     'high':'High',
                     'low':'Low',
                     'volume':'Volume',
                     })

df.isna().sum()

"""No null values in the dataset

"""

df.loc[df.duplicated(subset = ['open'])]

df.query('open ==561.50')

"""##Feature Understanding
Unvariate Analysis
"""

ax = df['open'].value_counts().head(10).plot(kind ='bar',title = "Opening prices Counts")
ax.set_xlabel('Opening Prices')
ax.set_ylabel("Count")

ax1 = df['close'].plot(kind = 'kde', title = 'Closing prices')
ax1.set_xlabel("Closing price in years")

"""##Feature Relationships

"""

df.plot(kind = 'scatter', x ='open',y='close')
plt.show()

sns.scatterplot(x ='open', y ='volume',data = df.head(100))

sns.pairplot(df, vars =['open','close','volume','high'])
plt.show()

df.columns

df_corr = df[['open', 'high', 'low', 'close', 'adjusted close', 'volume']].dropna().corr()

sns.heatmap(df_corr, annot = True)

"""##Ask Questions about the data
1)What was the highest opening price of this stock?
"""

sorted_df = df.sort_values('open', ascending = False)
highest_open = sorted_df.iloc[0]['open']
highest_open

df = df[['open', 'high', 'low', 'close', 'adjusted close', 'volume']]
df.shape

df.to_csv('Stock.csv',index=True)

df_c =df[['open','close']].dropna().corr()
sns.heatmap(df_c, annot = True)