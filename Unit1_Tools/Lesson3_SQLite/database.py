# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 14:30:28 2016

@author: Holly
"""

# Goal: print out the cities in the cities table of the getting_started.db where July is the warmest month.
# Assumptions: getting_started.db SQLite database exists and is located in the same directory as this Python file. The getting_started.db database can be empty.

# import libraries
import sqlite3 as lite
import pandas as pd

# variable declarations

cities_var = (
    ('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA'),
    ('Washington', 'DC'),
    ('Houston', 'TX'),
    ('Las Vegas', 'NV'),
    ('Atlanta', 'GA')
    )
                   
# Temperature values are annual average high temperatures in degrees Fahrenheit from http://www.usclimatedata.com/
weather_var = (
    ('New York City', 2013, 'July', 'January', 62),
    ('Boston', 2013, 'July', 'January', 59),
    ('Chicago', 2013, 'July', 'January', 59),
    ('Miami', 2013, 'August', 'January', 84),
    ('Dallas', 2013, 'July', 'January', 77),
    ('Seattle', 2013, 'July', 'January', 60),
    ('Portland', 2013, 'July', 'December', 63),
    ('San Francisco', 2013, 'September', 'December', 64),
    ('Los Angeles', 2013, 'September', 'December', 72),
    ('Washington', 2013, 'July', 'January', 65),
    ('Houston', 2013, 'July', 'January', 78),
    ('Las Vegas', 2013, 'July', 'December', 80),
    ('Atlanta', 2013, 'July', 'January', 70)
    )


# connect to database

# con is the connection object to the SQLite database called getting_started.db
con = lite.connect('getting_started.db')

with con:

    # cur is the cursor object which is obtained from calling the .cursor method on the connection object, con
    cur = con.cursor()
    
    # create the cities and weather tables, dropping old versions (which might be corrupt) if they exist
    cur.execute("DROP TABLE IF EXISTS cities")
    cur.execute("DROP TABLE IF EXISTS weather")   
    
    cur.execute("CREATE TABLE cities (name text, state text)")
    cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, ann_avg_high integer)")
        
    # insert data into the two tables, row by row, passing tuples to the .executemany method
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities_var)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather_var)

    # join the data together
    cur.execute("SELECT name, state, year, warm_month, cold_month, ann_avg_high FROM cities INNER JOIN weather ON name = city")
    
    # load into a pandas DataFrame
    rows = cur.fetchall()  # store all rows of data in the "rows" variable
    cols = [desc[0] for desc in cur.description]  # get the column/field names from the cur.description attribute where the names of the columns are in the first position, the 0th spot.
    df = pd.DataFrame(rows, columns=cols)


# print out the resulting city and state in a full sentence.  "The cities that are warmest in July are: ..."

# subset the dataframe to include only those records where July is the warmest month of the year.
warm_July = df[df.warm_month == 'July']

#convert the subsetted dataframe into a dictionary
warm_dict = warm_July.set_index('name')['state'].to_dict()

warm_str = ''
for city in warm_dict:
    warm_str = warm_str + city + ', ' + warm_dict.get(city) + ', '
    
final_str = warm_str[:-2]

print('The cities that are warmest in July are: ' + final_str + '.')