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
# import numpy as np
import seaborn as sns
# import matplotlib.pyplot as plt
# import plotly.plotly as py
# import plotly
# import plotly.graph_objs as go

# Create cities dictionary to include cities of interest and their locations
cities = {"Atlanta": '33.755960,-84.390304',
          "Austin": '30.265327,-97.743788',
          "Boston": '42.358056,-71.063611',
          "Denver": '39.761850,-104.881105',
          "Los Angeles": '34.050000,-118.250000',
          # "San Francisco": '37.783333,-122.416667',
          "Seattle": '47.609722,-122.333056'
          }

# Initialize a few key variables.  The start date is 30 days before now;
# "num_days" holds this 30-day value.
num_days = 30
start_date = datetime.datetime.now() - datetime.timedelta(days=num_days)
APIKEY = "2afe41b558da0181d1a9483c41f42df8"


# Create a connection object, con, which is the connection to the SQLite data-
# base "weather.db". (If weather.db does not exist, SQLite3 will create it.)
con = lite.connect('weather.db')
with con:
    # cur is the cursor object which is obtained from calling the .cursor
    # method on the connection object, con
    cur = con.cursor()
    # create the temperature table, dropping the old version if it exists
    # (in case it is corrupt)
    cur.execute("DROP TABLE IF EXISTS temperature")
    cur.execute("CREATE TABLE temperature \
    (city text, tmax float, tmax_time integer)")


# get forcast for all the cities
for city_var, latLong in cities.iteritems():
    date = start_date     # initialize the date variable
    # for each city, loop through past 30 days to get the weather data for that
    # day and store in dataframe
    # Within the loop, convert start_date to proper format for URL.
    '''I chose to use the [YYYY]-[MM]-[DD]T[HH]:[MM]:[SS] format which uses
    local time at each location as opposed to a UNIX time (seconds since
    midnight GMT on 1 Jan 1970) since to compare climatic data (like
    temperature swings) in the various cities which are in different time
    zones, local time is needed to ensure the same windows of temperature
    ranges.  For example the warmest hours of the day are typically 2-5 pm
    local time, so in order to compare apples to apples, the 2-5 pm range for
    Boston should be compared to the 2-5 pm range for San Francisco which is 3
    hours behind Boston.  If UNIX time were used, when it is 2 pm in Boston,
    it is 11 am in San Francisco and likely cooler than it will be at 2 pm
    San Francisco time later that same day.  Though a monthly average will be
    calculated, the period over which the average is calculated should be
    comparable so the data should be in local time.'''
    for i in range(0, num_days):  # beginning of date loop
        date_str = (date.strftime('%Y') + '-' + date.strftime('%m') + '-' +
                    date.strftime('%d') + 'T' + date.strftime('%H') + ':' +
                    date.strftime('%M') + ':' + date.strftime('%S'))

        url = ('https://api.forecast.io/forecast/' + APIKEY + '/' + latLong +
               ',' + date_str)

        r = requests.get(url)  # issue the request
        # load the contents of r.text into a response dict using json.loads()
        response_dict = json.loads(r.text)

        # temperatureMax and time are part of the "daily" data block.
        # See API info: https://developer.forecast.io/docs/v2#time_call
        tmax_var = response_dict['daily']['data'][0]['temperatureMax']
        tmax_time_var = response_dict['daily']['data'][0]['temperatureMaxTime']

        # convert time of max temperature from UNIX time to standard format
        tmax_time_var_std = (datetime.datetime.fromtimestamp
                             (int(tmax_time_var))
                             .strftime('%Y-%m-%d %H:%M:%S'))

        # connect to weather database to store data in the temperature table
        con = lite.connect('weather.db')
        with con:
            cur = con.cursor()
            #   insert data into the temperature table
            cur.execute("INSERT INTO temperature (city, tmax, tmax_time) \
            VALUES (?, ?, ?)", (city_var, tmax_var, tmax_time_var_std))

            # select all rows
            cur.execute("SELECT * FROM temperature")

            # load into a pandas DataFrame for future calculations
            # store all rows of data in the "rows" variable
            rows = cur.fetchall()

            # get the column names from the cur.description attribute
            # which are in the first position, the 0th spot.
            cols = [desc[0] for desc in cur.description]

            df = pd.DataFrame(rows, columns=cols)

        date = date + datetime.timedelta(days=1)
        # end of date loop - one city done, move on to the next city

    # print statement for debugging
    # print('Just finished collecting and storing data for ' + city_var)

    # end of city loop - all cities should have been processed

'''Calculate summary statistics over the 30-day period and store in a new
dataframe, "df_summary"; separate the latitude and longitude into two columns
converting them from strings to floats; then write the DataFrame to a .csv
file called "summary.csv".'''
df_summary = pd.DataFrame(columns=('city', 'long', 'lat', 'max_tmax',
                                   'min_tmax', 'range_tmax', 'mean_tmax',
                                   'sd_tmax'))

df_summary['max_tmax'] = df.groupby('city')['tmax'].max()
df_summary['min_tmax'] = df.groupby('city')['tmax'].min()
df_summary['mean_tmax'] = df.groupby('city')['tmax'].mean()
df_summary['sd_tmax'] = df.groupby('city')['tmax'].std()
df_summary['range_tmax'] = df_summary['max_tmax'] - df_summary['min_tmax']
df_summary['city'] = df_summary.index

for k, v in cities.iteritems():
    location = tuple(float(x) for x in v.split(','))
    df_summary.set_value(k, 'lat', location[0])
    df_summary.set_value(k, 'long', location[1])

df_summary.to_csv('summary.csv', index=False)

'''
# To plot the data via box plots, each city's 30-days of data needs to be
# separated out into its own DataFrame.
df_Atlanta = df[df.city == 'Atlanta']
df_Austin = df[df.city == 'Austin']
df_Boston = df[df.city == 'Boston']
df_Denver = df[df.city == 'Denver']
df_LosAngeles = df[df.city == 'Los Angeles']
# df_SanFrancisco = df[df.city == 'San Francisco']
df_Seattle = df[df.city == 'Seattle']

# Create a box plot for each city using the plotly library.
# plotly.offline.init_notebook_mode()

x_data = ['Atlanta',
          'Austin',
          'Boston',
          'Denver',
          'Los Angeles',
          # 'San Francisco',
          'Seattle'
          ]

y_data = [df_Atlanta['tmax'],
          df_Austin['tmax'],
          df_Boston['tmax'],
          df_Denver['tmax'],
          df_LosAngeles['tmax'],
          # df_SanFrancisco['tmax'],
          df_Seattle['tmax']
          ]

colors = ['rgba(93, 164, 214, 0.5)',
          'rgba(255, 144, 14, 0.5)',
          'rgba(44, 160, 101, 0.5)',
          'rgba(255, 65, 54, 0.5)',
          'rgba(207, 114, 255, 0.5)',
          'rgba(127, 96, 0, 0.5)']

traces = []

for xd, yd, cls in zip(x_data, y_data, colors):
        traces.append(go.Box(
            y=yd,
            name=xd,
            boxpoints='all',
            jitter=0.5,
            whiskerwidth=0.2,
            fillcolor=cls,
            marker=dict(
                size=2,
            ),
            line=dict(width=1),
        ))

layout = go.Layout(
    title='Maximum Daily Temperature (deg F) for the Last 30 Days',
    yaxis=dict(
        autorange=True,
        showgrid=True,
        zeroline=True,
        dtick=5,
        gridcolor='rgb(255, 255, 255)',
        gridwidth=1,
        zerolinecolor='rgb(255, 255, 255)',
        zerolinewidth=2,
    ),
    margin=dict(
        l=40,
        r=30,
        b=80,
        t=100,
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
    showlegend=False
)

fig = go.Figure(data=traces, layout=layout)
plotly.plotly.iplot(fig)

# not using
# plotly.offline.plot(fig)
# plotly.tools.embed("https://plot.ly/~streaming-demos/4")
'''
# Create a box plot for each city using the seaborn library.
sns.set_style("whitegrid")
ax = sns.boxplot(x="city", y="tmax", data=df.sort_values(by='city'))
ax = sns.swarmplot(x="city", y="tmax", data=df.sort_values(by='city'),
                   color=".25")
