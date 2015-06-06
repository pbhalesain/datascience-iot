
# coding: utf-8

#### In this series we will be using the following packages

# In[1]:

get_ipython().magic(u'matplotlib inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# To Convert a series object of date-like objects we can use the to_datetime function

# In[4]:

pd.to_datetime(pd.Series(['Sep 24, 1979', '2014-05-08']))


# In many cases the easiest way is more to associate objects with a time span

# In[5]:

periods = pd.PeriodIndex([pd.Period("2015-02"), pd.Period("2015-04"), 
                          pd.Period("2015-06")])
periods


# In[6]:

info = pd.Series([2.4,7.6,4.5], periods)
info.plot()


# If we need timestamps on a regular frequency we can use the pandas function date_range. In this case the frequence of the data is one month(freq='M')

# In[9]:

Months = pd.date_range("2013-10","2015-01", freq="M")
Months


# We can use it with a table of prices

# In[10]:

Prices = np.array([23.4,23.1, 23.2, 23.4, 23.1, 23.8, 24, 23.9, 23.7, 24.2, 24.5, 24.9, 25, 24.9, 25.1])
info = pd.Series(Prices, index=Months)
info.plot()


# we can select a time span between march and september

# In[11]:

info["2014-03": "2014-09"].plot()


# We can access a specific value

# In[12]:

info["2013"]


# In[13]:

info["2014-06"]


# Now on we will be using yahoo API for python and execute a more practical example

# In[16]:

from yahoo_finance import Share


# 
# Stock pricess (Apple) between '2014-04-27' and '2014-04-29'
# 

# In[18]:

yahoo = Share('AAPL')
data = yahoo.get_historical('2014-04-27', '2014-04-29')
data


# Plotting data for the time span between '2014-03-01' and '2014-04-29'

# In[19]:

data = yahoo.get_historical('2014-03-01', '2014-04-29')
Close_values = []
for value in data :
    Close_values.append(value["Adj_Close"])
plt.plot(Close_values)
plt.title("Close")
plt.show()


# In[36]:

import datetime
import matplotlib.dates as mdates

def yahoo():
    yahoo = Share("IBM")
    data = yahoo.get_historical('2014-04-05', '2014-04-29')
    return data

def data_frame():
    yahoo_data = yahoo()
    pandas_data = pd.DataFrame(columns = ["Adj_Close", "Close", "Date"
                                          "High", "Low", "Open", "Symbol", "Volume"])
    for i in range(len(yahoo_data)):
        pandas_data = pandas_data.append({"Adj_Close":yahoo_data[i]["Adj_Close"],
                                        "Close":yahoo_data[i]["Close"],
                                        "Date":yahoo_data[i]["Date"],
                                        "High":yahoo_data[i]["High"],
                                        "Low":yahoo_data[i]["Low"],
                                        "Open":yahoo_data[i]["Open"],
                                        "Symbol":yahoo_data[i]["Symbol"],
                                        "Volume":yahoo_data[i]["Volume"]
                                        }, ignore_index=True )
    return pandas_data

def time_series():
    pandas_data = data_frame()
    
    days = pandas_data["Date"]
    dates = [datetime.datetime.strptime(day, '%Y-%m-%d') for day in days]
    close_values = pandas_data["Close"]
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    ax.set_xticks(dates)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    ax.plot_date(dates, close_values, ls='-', marker='o')
    ax.set_title('Close Values')
    ax.set_ylabel('Prices')
    ax.grid(True)
    
    fig.autofmt_xdate(rotation=45)
    fig.tight_layout()
    fig.show()

time_series()
    


# In[39]:

def time_series_error():
    
    pandas_data = data_frame()
        
    Days = pandas_data["Date"]
    Dates = [datetime.datetime.strptime(day, '%Y-%m-%d') for day in Days]
    Close_Values = pandas_data["Close"].astype(float)
    
    error=np.zeros(len(Close_Values))

    try:
        for i in np.arange(1,len(Close_Values),1):
            error[i] = Close_Values[i+1] - Close_Values[i]
    except Exception as e:
        pass

    error
    
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_xticks(Dates)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))

    ax.plot_date(Dates, error, ls='-', marker='o')
    ax.set_title('Close Values')
    ax.set_ylabel('Error')
    ax.grid(True)

    fig.autofmt_xdate(rotation=45)
    fig.tight_layout()

    fig.show()

time_series_error()


# In[ ]:



