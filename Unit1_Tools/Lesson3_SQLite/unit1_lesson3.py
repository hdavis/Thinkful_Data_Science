# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 12:02:02 2016

@author: Holly
"""


# these commands seem to work better directly in the terminal, not in the iPython console...since they aren't python commands, they are SQL commands!
sqlite3 getting_started.db


> .tables
> .indices
> .schema


CREATE TABLE cities (name text, state text);

INSERT INTO cities (name, state) VALUES
    ('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA');
    
# Try it section:    
CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer);    

# insert rows into weather table
INSERT INTO weather (city, year, warm_month, cold_month, average_high) VALUES
    ('New York City', 2013, 'July', 'January', 62),
    ('Boston', 2013, 'July', 'January', 59),
    ('Chicago', 2013, 'July', 'January', 59),
    ('Miami', 2013, 'August', 'January', 84),
    ('Dallas', 2013, 'July', 'January', 77),
    ('Seattle', 2013, 'July', 'January', 61),
    ('Portland', 2013, 'July', 'December', 63),
    ('San Francisco', 2013, 'September', 'December', 64),
    ('Los Angeles', 2013, 'September', 'December', 75);

    
    
    # %% WRITING QUERIES ON YOUR DATA (I.E. READING THE DATA IN THE DATABASE)
    
SELECT * FROM cities;
    
SELECT name, state FROM cities;

SELECT name, state FROM cities WHERE state='CA';

SELECT name FROM cities WHERE name LIKE '%le%'; # LIKE means contains the substring between the two %s which are wildcard characters.

SELECT name FROM cities LIMIT 2 OFFSET 3; # LIMIT = # of rows that will be returned; OFFSET = how many rows to skip which match the query to give an offset in the data.

SELECT COUNT(*) FROM cities WHERE name LIKE 'San%' AND state='CA';

# %% Try it! for SQL queries

# How many rows are in the weather table?
SELECT COUNT(*) FROM weather WHERE year=2013;
# 9

# What cities were hottest in July in 2013?
SELECT city FROM weather WHERE warm_month='July';
#New York City
#Boston
#Chicago
#Dallas
#Seattle
#Portland


# What cities were hottest in July and not coldest in January?
SELECT city FROM weather WHERE warm_month='July' AND cold_month!='January';
# Portland

# The first two cities which were coldest in January
SELECT city FROM weather WHERE cold_month='January' LIMIT 2;
# New York City
# Boston

# %% Updating data
UPDATE cities SET state='Californ-I-A' WHERE state='CA';

UPDATE cities SET state='CA' WHERE state='Californ-I-A';

DELETE FROM cities where state='CA';

DELETE FROM cities where state='NY';
DELETE FROM cities where state='MA';
DELETE FROM cities where state='IL';
DELETE FROM cities where state='FL';
DELETE FROM cities where state='TX';
DELETE FROM cities where state='WA';
DELETE FROM cities where state='OR';

INSERT INTO cities (name, state) VALUES
    ('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA');

# %% Export data to CSV

# export cities table

# switch output mode to CSV
.mode csv

# turn on the column headers
.headers on

# output any statements to the cities.csv file using the .output command
.output cities.csv

# query to select all of the rows from the cities table (and write it to the csv file since the line before indicated where to write the rows)
select * from cities;

# I assume all the rows were already written and switch output mode from csv back into command line mode
.output stdout


# NOTE THE RESULTING .CSV FILE HAS QUOTES AROUND THE CITIES WITH MORE THAN ONE WORD (NEW YORK CITY, SAN FRANCISCO AND LOS ANGELES)  
# HAVE NOT YET FIGURED OUT THE RIGHT SYNTAX TO FIX THIS PROBLEM.
# MAYBE USE AN OPTION quote=FALSE to eliminate quotes or quote = TRUE to get all items to have quotes...

# %% Import data from CSV

create table cities_copy (name text, state text);
.tables

.separator ","

.import cities.csv cities_copy
select * from cities_copy;
  

# %%
# Assignment 2

# The sqlite3 module is used to work with the SQLite database.
import sqlite3 as lite

# Here you connect to the database. The `connect()` method returns a connection object.
con = lite.connect('getting_started.db')

with con:
  # From the connection, you get a cursor object. The cursor is what goes over the records that result from a query.
  cur = con.cursor()    
  cur.execute('SELECT SQLITE_VERSION()')
  # You're fetching the data from the cursor object. Because you're only fetching one record, you'll use the `fetchone()` method. If fetching more than one record, use the `fetchall()` method.
  data = cur.fetchone()
  # Finally, print the result.
  print("SQLite version: %s" % data)
  
 # %% Inserting data - rows_sqlite.py
  
import sqlite3 as lite

con = lite.connect('getting_started.db')

# Inserting rows by passing values directly to `execute()`
with con:

    cur = con.cursor()
    cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
    cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
    cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January')")
    cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January')")

# get error: "OperationalError: table weather has 5 columns but 4 values were supplied"
# reason for error, no temerature data supplied as 5th column.

# %% redoing the code above to add in the 5th column...

import sqlite3 as lite

# con is the connection object to the SQLite database called getting_started.db
con = lite.connect('getting_started.db')

# Inserting rows by passing values directly to `execute()`
with con:
    # cur is the cursor object which is obtained from calling the .cursor method on the connection object, con
    cur = con.cursor()
    cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
    cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
    cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January', 59)")
    cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January', 78)")

# %%  WRONG CODE FOR THE WEATHER DATA - NEED 5 COLUMNS OF DATA, NOT 4

import sqlite3 as lite

cities_var = (('Las Vegas', 'NV'),
                    ('Atlanta', 'GA'))

weather_var = (('Las Vegas', 2013, 'July', 'December'),
                     ('Atlanta', 2013, 'July', 'January'))

con = lite.connect('getting_started.db')

# Inserting rows by passing tuples to `execute()`
with con:

    cur = con.cursor()
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities_var)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?)", weather_var)


# %% FIXING PROBLEM ABOVE - Correct code is: 
weather_var = (('Las Vegas', 2013, 'July', 'December', 50),
                     ('Atlanta', 2013, 'July', 'January', 70))
with con:
    
    cur = con.cursor()
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather_var)

# %% Retrieving Data

# retrieve and print

import sqlite3 as lite

con = lite.connect('getting_started.db')

with con:    

    cur = con.cursor()
    cur.execute("SELECT * FROM cities")

    rows = cur.fetchall()

    for row in rows:
        print(row)

# %% Retrieving Data

# retrieve and store in a Pandas dataframe - not quite there yet...

import sqlite3 as lite
import pandas as pd

# con is the connection object to the SQLite database called getting_started.db
con = lite.connect('getting_started.db')

# Select all rows and print the result set one row at a time
with con:

    # cur is the cursor object which is obtained from calling the .cursor method on the connection object, con
    cur = con.cursor()
    cur.execute("SELECT * FROM cities")

    rows = cur.fetchall()
    df = pd.DataFrame(rows)

df.head() # gives first 5 rows and shows that our column names are 0 and 1 right now.

# %% Retrieving Data

# retrieve and store in a Pandas dataframe ++++++++++++++++++++++++++++++

import sqlite3 as lite
import pandas as pd

# con is the connection object to the SQLite database called getting_started.db
con = lite.connect('getting_started.db')

# Select all rows and print the result set one row at a time
with con:

    # cur is the cursor object which is obtained from calling the .cursor method on the connection object, con
    cur = con.cursor()
    cur.execute("SELECT * FROM cities")  # select all rows of getting_started.db

    rows = cur.fetchall()  # store all rows of data in the "rows" variable
    cols = [desc[0] for desc in cur.description]  # get the column/field names from the cur.description attribute where the names of the columns are in the first position, the 0th spot.
    df = pd.DataFrame(rows, columns=cols)

# %% Joining and filtering data in SQLite

# need to type the following commands into Terminal once you've started SQLite3 
# to open an EXISTING database, type sqlite3 database_name.db at the Terminal command line prompt within the folder where the database resides.

sqlite3 getting_started.db
# check out data
.tables
.schema # to get the names of the fields in both tables
# result of .schema command is:
# CREATE TABLE cities (name text, state text);
#CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer);


SELECT name, state, year, warm_month, cold_month, average_high FROM cities INNER JOIN weather ON name = city;
# not completely positive on indentation convention - believe this is a single command (not two separate commands).

SELECT warm_month, AVG(average_high) FROM weather GROUP BY warm_month;

# Try it: Write a SQL statement which finds the mean of the average high temperatures for all of the cities within a state.
# Have to do join first.
SELECT name, state, average_high FROM cities INNER JOIN weather ON name = city, AVG(average_high) FROM weather GROUP BY state; # did not work

# TRYING TO SAVE JOIN TO A NEW TABLE FIRST, THEN DO GROUP BY
CREATE TABLE weather_w_state AS SELECT name, state, year, warm_month, cold_month, average_high FROM cities INNER JOIN weather ON name = city;

SELECT state, AVG(average_high) FROM weather_w_state GROUP BY state;
# WORKS!

# Doing with out creating table first: - USE THIS
SELECT state, AVG(average_high) FROM cities INNER JOIN weather ON name = city GROUP BY state;


# ORDER BY
SELECT city, average_high FROM weather ORDER BY average_high;

# List in descending order...
SELECT city, average_high FROM weather ORDER BY average_high DESC;

# Try it:
#Write a query which which finds the mean of the average high temperatures for all of the cities within a state, starting with the hottest.
SELECT state, AVG(average_high) FROM weather_w_state GROUP BY state ORDER BY average_high DESC;

# Try it without creating weather_w_state table first: - USE THIS
SELECT state, AVG(average_high) FROM cities INNER JOIN weather ON name = city GROUP BY state ORDER BY average_high DESC;




SELECT warm_month, AVG(average_high) FROM weather GROUP BY warm_month HAVING AVG(average_high) > 65;

# Try it: Write a query which which finds the mean of the average high temperatures for all of the cities within a state, starting with the hottest, and filtering out states with a mean above 65F.
SELECT state, AVG(average_high) FROM weather_w_state GROUP BY state HAVING AVG(average_high) > 65 ORDER BY average_high DESC;

# Try it without creating weather_w_state table first: - USE THIS
SELECT state, AVG(average_high) FROM cities INNER JOIN weather ON name = city GROUP BY state HAVING AVG(average_high) > 65 ORDER BY average_high DESC;


