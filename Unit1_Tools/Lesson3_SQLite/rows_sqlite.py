# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 15:43:09 2016

@author: Holly
"""

import sqlite3 as lite

# con is the connection object to the SQLite database called getting_started.db
con = lite.connect('getting_started.db')

# Inserting rows by passing values directly to `execute()`
with con:

# cur is the cursor object which is obtained from calling the .cursor method on the connection object, con
    cur = con.cursor()
    cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
    cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
    cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January')")
    cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January')")
