# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 10:11:00 2016

@author: Holly
"""
# import libraries
import datetime
import requests
import json
import sqlite3 as lite
import pandas as pd

cities = {"Atlanta": '33.762909,-84.422675',
          "Boston": '42.331960,-71.020173',
          "Denver": '39.761850,-104.881105',
          "Los Angeles": '34.019394,-118.410825',
          "San Francisco": '37.727239,-123.032229',
          "Seattle": '47.620499,-122.350876'
          }

APIKEY = "2afe41b558da0181d1a9483c41f42df8"

# ----------------------------------------------------------
#latLong = cities["San Francisco"] 

now = datetime.datetime.now()
start_date = now - datetime.timedelta(days=30)

# convert start_date to proper format for URL.
# Chose to use the [YYYY]-[MM]-[DD]T[HH]:[MM]:[SS] format which uses local time at each location as opposed to a UNIX time (seconds since midnight GMT on 1 Jan 1970) since to compare climatic data (like temperature swings) in the various cities which are in different time zones, local time is needed to ensure the same windows of temperature ranges.  For example the warmest hours of the day are typically 2-5 pm local time, so in order to compare apples to apples, the 2-5 pm range for Boston should be compared to the 2-5 pm range for San Francisco which is 3 hours behind Boston.  If UNIX time were used, when it is 2 pm in Boston, it is 11 am in San Francisco and likely cooler than it will be at 2 pm San Francisco time later that same day.  Though a monthly average will be calculated, the period over which the average is calculated should be comparable so the data should be in local time.
start_date_str = start_date.strftime('%Y') + '-' + start_date.strftime('%m') + '-' + start_date.strftime('%d') + 'T' + start_date.strftime('%H') + ':' + start_date.strftime('%M') + ':' + start_date.strftime('%S')

# url = 'https://api.forecast.io/forecast/' + APIKEY + '/' + latLong + ',' + start_date_str
con = lite.connect('weather.db')

with con:

    # cur is the cursor object which is obtained from calling the .cursor method on the connection object, con
    cur = con.cursor()
    
    # create the cities and weather tables, dropping old versions (which might be corrupt) if they exist
    cur.execute("DROP TABLE IF EXISTS temperature")   
    cur.execute("CREATE TABLE temperature (city text, tmax float, tmax_time integer)")
con.close()    
    
date = start_date
# %%
# get forcast for cities
for city_var in cities:
    latLong = cities[city_var]
    city_text = city_var
    print("Getting data for", city_var)
    print ("Lat and Long are", latLong)

#latLong = cities['San Francisco']

    # for each city, loop through past 30 days to get the weather data for that day and store in dataframe
    for i in range(0, 30):
        date_str = date.strftime('%Y') + '-' + date.strftime('%m') + '-' + date.strftime('%d') + 'T' + date.strftime('%H') + ':' + date.strftime('%M') + ':' + date.strftime('%S')
            
        url = 'https://api.forecast.io/forecast/' + APIKEY + '/' + latLong + ',' + date_str
    
        r = requests.get(url)  # issue the request
    # read relevant data in
    # write to SQLite database in appropriate format
    
#r.text

        a = r.text

# load the contents of r.text into a response dictionary using json.loads()
        response_dict = json.loads(a)

# response_dict.keys()

        tmax_var = response_dict['daily']['data'][0]['temperatureMax']
        tmax_time_var = response_dict['daily']['data'][0]['temperatureMaxTime']
        print('Just finished getting t-max for', city_var)

#weather_data = (tmax_var, tmax_time_var)




# "offset":-7
# "temperatureMax":57.14,"temperatureMaxTime":1463634000
# "units":"us"

#Developers are strongly encouraged, therefore, to check for the presence of data before attempting to read it.
# temperatureMax and time are part of the "daily" data block.  See API info: https://developer.forecast.io/docs/v2#time_call

# create a connection object, con, which is the connection to the SQLite database "weather.db" (If weather.db does not exist, SQLite3 will create it.)
        con = lite.connect('weather.db')

        with con:

            # cur is the cursor object which is obtained from calling the .cursor method on the connection object, con
            cur = con.cursor()
    
            cur.execute("INSERT INTO temperature (city, tmax, tmax_time) VALUES (?, ?, ?)", (city_text, tmax_var, tmax_time_var))
            #   insert data into the temperature table
            #    cur.execute("INSERT INTO temperature VALUES(tmax_var, tmax_time_var)")
   

 

            ###  cur.execute("insert into contacts (name, phone, email) values (?, ?, ?)", (name, phone, email))
            
            
            # insert data into the two tables, row by row, passing tuples to the .executemany method
        
            ####        cur.executemany("INSERT INTO temperature VALUES(?,?)", weather_data)

            # select all rows
            cur.execute("SELECT * FROM temperature")
    
            # load into a pandas DataFrame
            rows = cur.fetchall()  # store all rows of data in the "rows" variable
            cols = [desc[0] for desc in cur.description]  # get the column/field names from the cur.description attribute where the names of the columns are in the first position, the 0th spot.
            df = pd.DataFrame(rows, columns=cols)
            
        con.close()
         
        date = date + datetime.timedelta(days=1)
        print('just wrote t-max data to weather database.')
        # end of date loop - one city done, move on to the next city
    
# to get date from unix time back into human readable time
# print(datetime.datetime.fromtimestamp(int('1463634000')).strftime('%Y-%m-%d %H:%M:%S'))
# 2016-05-18 01:00:00