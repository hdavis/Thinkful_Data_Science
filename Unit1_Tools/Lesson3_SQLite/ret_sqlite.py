# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 20:44:53 2016

@author: Holly
"""

import sqlite3 as lite

con = lite.connect('getting_started.db')

with con:    

    cur = con.cursor()    
    cur.execute("SELECT * FROM cities")

    rows = cur.fetchall()

    for row in rows:
        print(row)