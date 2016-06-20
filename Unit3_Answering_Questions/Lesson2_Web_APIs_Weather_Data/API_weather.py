# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 10:11:00 2016

@author: Holly
"""

cities = {"Atlanta": '33.762909,-84.422675',
          "Boston": '42.331960,-71.020173',
          "Denver": '39.761850,-104.881105',
          "Los Angeles": '34.019394,-118.410825',
          "San Francisco": '37.727239,-123.032229',
          "Seattle": '47.620499,-122.350876'
          }

# The Dark Sky Forecast API
# gmail, L2I3F!

APIKEY = 2afe41b558da0181d1a9483c41f42df8

# forcast at Alcatraz
https://api.forecast.io/forecast/2afe41b558da0181d1a9483c41f42df8/37.8267,-122.423

https://api.forecast.io/forecast/APIKEY/LATITUDE,LONGITUDE,TIME

#time is Unix or YYYY-MM-DDThh:mm:ss

Load datetime package??

datetime.datetime.now()

datetime.timedelta()

# %%
import datetime

cities = {"Atlanta": '33.762909,-84.422675',
          "Boston": '42.331960,-71.020173',
          "Denver": '39.761850,-104.881105',
          "Los Angeles": '34.019394,-118.410825',
          "San Francisco": '37.727239,-123.032229',
          "Seattle": '47.620499,-122.350876'
          }

APIKEY = "2afe41b558da0181d1a9483c41f42df8"

#latLong = cities["San Francisco"]

start_date = datetime.datetime.now() - datetime.timedelta(days=30)

# url = 'https://api.forecast.io/forecast/' + APIKEY + '/' + latLong
# + ',' + start_date

# convert start_date to proper format for URL.
# Chose to use the [YYYY]-[MM]-[DD]T[HH]:[MM]:[SS] format which uses local time at each location as opposed to a UNIX time (seconds since midnight GMT on 1 Jan 1970) since to compare climatic data (like temperature swings) in the various cities which are in different time zones, local time is needed to ensure the same windows of temperature ranges.  For example the warmest hours of the day are typically 2-5 pm local time, so in order to compare apples to apples, the 2-5 pm range for Boston should be compared to the 2-5 pm range for San Francisco which is 3 hours behind Boston.  If UNIX time were used, when it is 2 pm in Boston, it is 11 am in San Francisco and likely cooler than it will be at 2 pm San Francisco time later that same day.  Though a monthly average will be calculated, the period over which the average is calculated should be comparable so the data should be in local time.


# start_string = str(start_date) # date format not quite right

# 2013-05-06T12:00:00

# Following does not add leading 0 for single-digit values (May is 5 not 05 and 05 is required)
#start_date_str = str(start_date.year) + '-' + str(start_date.month) + '-' + str(start_date.day) + 'T' + str(start_date.hour) + ':' + str(start_date.minute) + ':' + str(start_date.second)


start_date_str = start_date.strftime('%Y') + '-' + start_date.strftime('%m') + '-' + start_date.strftime('%d') + 'T' + start_date.strftime('%H') + ':' + start_date.strftime('%M') + ':' + start_date.strftime('%S')


# other options for formatting to get 0 in front of 5 using March as the month.  From this webpage: http://stackoverflow.com/questions/15509345/python-datetime-extract-double-digit-month-and-day-values
# In [5]: '{:02d}'.format(d.month)
# Out[5]: '03'

# In [6]: '%02d' % d.month
# Out[6]: '03'

# In [7]: d.strftime('%m')
# Out[7]: '03'


url = 'https://api.forecast.io/forecast/' + APIKEY + '/' + latLong + ',' + start_date_str


# to get date from unix time back into human readable time
#print(datetime.datetime.fromtimestamp(int("1463558400")).strftime('%Y-%m-%d %H:%M:%S'))
# 2016-05-18 01:00:00

# issue the request
import requests
r = requests.get(url)
r.text

# %%
# get forcast for cities
for city in cities:
    latLong = cities[city]
    url = 'https://api.forecast.io/forecast/' + APIKEY + '/' + latLong + ',' + start_date_str
    r = requests.get(url)
    # read relevant data in
    # write to SQLite database in appropriate format