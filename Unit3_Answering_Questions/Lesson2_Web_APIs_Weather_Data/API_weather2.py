# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 10:11:00 2016

@author: Holly
"""

import datetime
import requests
import json

cities = {"Atlanta": '33.762909,-84.422675',
          "Boston": '42.331960,-71.020173',
          "Denver": '39.761850,-104.881105',
          "Los Angeles": '34.019394,-118.410825',
          "San Francisco": '37.727239,-123.032229',
          "Seattle": '47.620499,-122.350876'
          }

APIKEY = "2afe41b558da0181d1a9483c41f42df8"

# ----------------------------------------------------------
latLong = cities["San Francisco"] 

start_date = datetime.datetime.now() - datetime.timedelta(days=30)

# convert start_date to proper format for URL.
# Chose to use the [YYYY]-[MM]-[DD]T[HH]:[MM]:[SS] format which uses local time at each location as opposed to a UNIX time (seconds since midnight GMT on 1 Jan 1970) since to compare climatic data (like temperature swings) in the various cities which are in different time zones, local time is needed to ensure the same windows of temperature ranges.  For example the warmest hours of the day are typically 2-5 pm local time, so in order to compare apples to apples, the 2-5 pm range for Boston should be compared to the 2-5 pm range for San Francisco which is 3 hours behind Boston.  If UNIX time were used, when it is 2 pm in Boston, it is 11 am in San Francisco and likely cooler than it will be at 2 pm San Francisco time later that same day.  Though a monthly average will be calculated, the period over which the average is calculated should be comparable so the data should be in local time.
start_date_str = start_date.strftime('%Y') + '-' + start_date.strftime('%m') + '-' + start_date.strftime('%d') + 'T' + start_date.strftime('%H') + ':' + start_date.strftime('%M') + ':' + start_date.strftime('%S')

url = 'https://api.forecast.io/forecast/' + APIKEY + '/' + latLong + ',' + start_date_str

# to get date from unix time back into human readable time
# print(datetime.datetime.fromtimestamp(int('1463634000')).strftime('%Y-%m-%d %H:%M:%S'))
# 2016-05-18 01:00:00

# ----------------------------------------------------
# issue the request
#import requests
r = requests.get(url)
r.text

a = r.text

# import json
response_dict = json.loads(a)

response_dict.keys()

response_dict['daily']['data'][0]['temperatureMax']


# %%
# "offset":-7
# "temperatureMax":57.14,"temperatureMaxTime":1463634000
# "units":"us"

#Developers are strongly encouraged, therefore, to check for the presence of data before attempting to read it.
# temperatureMax and time are part of the "daily" data block.  See API info: https://developer.forecast.io/docs/v2#time_call

# SQLite experimentation - creating a database this way does not seem to work in the iPython console, but does work in the Terminal window (once in correct directory)
sqlite3 weather.db  # create empty weather SQLite database

# %%
# get forcast for cities
for city in cities:
    latLong = cities[city]
    url = 'https://api.forecast.io/forecast/' + APIKEY + '/' + latLong + ',' + start_date_str
    r = requests.get(url)  # issue the request
    # read relevant data in
    # write to SQLite database in appropriate format