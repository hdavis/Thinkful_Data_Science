# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:13:08 2016

@author: Holly
"""

# list of handy command line commands
pwd
ls
cd
mkdir
rmdir
cp
mv

ipython # starts an ipython shell

# Python List Interactions

li = [1, 2, 4, 3, 5]

# Select a range between index 1 and 3 (closed/open range, in math terms)
li[1:3]
# [2, 4]

# Omit the beginning or end
li[2:]
# [4, 3, 5]

li[:3]
# [1, 2, 4]

# Select every second entry (i.e. step by 2)
li[::2]
# [1, 4, 5]

# Reverse the list
li[::-1]
# [5, 3, 4, 2, 1]

# Note the syntax for the above is: li[start:end:step]
# Delete the 3rd item
del li[2]
li
# [1, 2, 3, 5]

# Check if 1 is in list li
1 in li
# True

# What's the length of the list li?
len(li)
# 4

# Lesson 1, Assignment 4: Controlling the Code Flow --------
import datetime

year = 1999

if 2001 <= year <= 2006:
    print("Lookout Records")
elif year >= 2007 and year <= 2009:
    print("Touch and Go Records")
elif 2010 <= year <= datetime.datetime.now().year:
    print("Matador Records")
elif year >= datetime.datetime.now().year:
    print("We don't know since we cannot look into the future")
else:
    print("Band did not yet exist")


# ------------------------

# Dictionary Exercise

actors = {
    "Kyle MacLachlan": "Dale Cooper",
    "Sheryl Lee": "Laura Palmer",
    "Lara Flynn Boyle": "Donna Hayward",
    "Sherilyn Fenn": "Audrey Horne"
}

# Loop over the following dictionary, printing out the name of the actor, and the character which they play:

for actor in actors:
    print(actor, actors.get(actor))

# returns:
# ('Sheryl Lee', 'Laura Palmer')
# ('Sherilyn Fenn', 'Audrey Horne')
# ('Lara Flynn Boyle', 'Donna Hayward')
# ('Kyle MacLachlan', 'Dale Cooper')

for actor in actors:
    print(actor + " = " + actors.get(actor))

# Returns
# Sheryl Lee = Laura Palmer
# Sherilyn Fenn = Audrey Horne
# Lara Flynn Boyle = Donna Hayward
# Kyle MacLachlan = Dale Cooper


miles_run = 0
running = True

while running:
    if miles_run <= 10:
        print("Still running! On mile {}".format(miles_run))
        miles_run += 1
    else:
        running = False
print("Whew! I'm tired")

# get same output as code below - do not appear to need the else (not sure why they put it in - to try to make the logic clearer for people learning? Actually makes it more confusing for me.)

miles_run = 0
running = True

while running:
    if miles_run <= 10:
        print("Still running! On mile {}".format(miles_run))
        miles_run += 1
    else:
        running = False
else:
    print("Whew! I'm tired")


# Use a while loop to solve the following problem: A slow, but determined, walker sets off from Leicester to cover the 102 miles to London at 2 miles per hour. Another walker sets off from London heading to Leicester going at 1 mile per hour. Where do they meet?
walker1 = 0
walker2 = 0
walking = True
total_miles = 102

while walking:
    if (total_miles-walker1) == walker2:
        print("We met this many miles from London: {}".format(walker2))
        walking = False
    else:
        walker1 += 2
        walker2 += 1


print("walking done")

# Try looking up Jamie Theakston in the following phone book. When it fails, catch the exception and print an appropriate error message.

phone_book = {
    "Sarah Hughes": "01234 567890",
    "Tim Taylor": "02345 678901",
    "Sam Smith":  "03456 789012"
}

# these work and returns Tim Taylor's number
phone_book.get("Tim Taylor")
phone_book["Tim Taylor"]


# this should not work
phone_book.get("Jamie Theakston")  # returned nothing
phone_book["Jamie Theakston"]

# throws an exception
person = "Jamie Theakston"
try:
    phone_book[person]
    print(person + "'s phone number is " + phone_book[person])
except KeyError:
    print(person + " is not in the phone book")

# prints out the person's phone number
person = "Tim Taylor"
try:
    phone_book[person]
    print(person + "'s phone number is " + phone_book[person])
except KeyError:
    print(person + " is not in the phone book")


# %%------------ Funcitons

import collections


# -- their example - has some useful code: datetime and .format()

from datetime import datetime
import logging


def log_handler(msg):
    """Sends msg to the logging platform"""
    date = str(datetime.now())
    msg = date + " - " + msg
    return logging.info(msg)


def log(msg):
    """A convenience function. Adds msg to the logs with log_handler"""
    msg = str(msg)
    print("Message logged: " + msg)
    return log_handler(msg)


def addition(a, b):
    """Adds two numbers and logs the result"""
    x = a + b
    log("Adding {0} and {1} = {2}.".format(a, b, x))
    return x

addition(1, 2)
addition(2, 3)
addition(5, addition(3, 5))

# %%-----------

# -------- Bake a Cake ------------------------------------

# Ingredients are stored as a dictionary of tuples. Each tuple contains the name
# of the ingredients and the amount in milliliters (unless otherwise specified)
# Why a dictionary of tuples? Because it is kinda convenient, and shows off how to
# combine multiple data structures.
ingredients = {
    "butter": ("butter", 118.3),
    "sugar": ("sugar", 236.6),
    "vanilla": ("vanilla", 4.929),
    "eggs": ("eggs", 2),  # whole eggs
    "cocoa": ("cocoa", 118.3),
    "flour": ("flour", 118.3)
}

# The butter was refrigerated, so it's not soft yet.
butter_soft = False

bowl = []


# To make the cake, we'll need the following functions
def melt(this):
    print("Melting {0}.".format(this))


def bake(this, temp):
    print("Baking {0} at {1}.".format(this, temp))


def mix(this):
    print("Mixing {0}.".format(this))


def add_to_bowl(ingredient):
    return bowl.append(ingredient)


# Start the algorithm!

if butter_soft != True:
    melt(ingredients["butter"][0])
    butter_soft = True

add_to_bowl(ingredients["butter"][0])
add_to_bowl(ingredients["sugar"][0])

mixing_time = 0
mixture_creamy = False

# Mix until creamy
while mixture_creamy == False:
    mix(bowl)
    mixing_time += 1
    if mixing_time == 3:
        # After 3 minutes, the mixture will be creamy,
        # and our while loop will stop
        mixture_creamy = True

add_to_bowl(ingredients["eggs"][0])
add_to_bowl(ingredients["vanilla"][0])

mix(bowl)

add_to_bowl(ingredients["cocoa"][0])
add_to_bowl(ingredients["flour"][0])

mixing_time = 0
well_blended = False

# Mix until well-blended
while well_blended == False:
    mix(bowl)
    mixing_time += 1
    if mixing_time == 4:
        well_blended = True

# In cooking terms: pour contents of the bowl into a cake pan
# In Python terms: redefine the bowl variable as cake_pan
cake_pan = bowl

cooking_temp = 350
cooking_time = 30

for minute in range(0, cooking_time):
    bake(cake_pan, cooking_temp)

print("Cake is done!")

# %%
# Fibonacci algorightm - The solution below is a recursive algorithm

# Fn = Fn-1 + Fn-2

# seed values F1 = 1 and F2 = 2
# or F1 = 0 and F2 = 1

# Following code does not work
# def F(n):
#    return F(n-2) + F(n-1)


# right way:
def F(n):
    if n < 2:
        return n
    else:
        return F(n-2) + F(n-1)


def F(n):
    if n < 2:
        print("n is less than 2")
        return n
    else:
        print("n is greater than or equal to 2")
        return F(n-2) + F(n-1)

# ---------- FizzBuzz Algorithm

for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print(i)
        print("Fizz")
    elif i % 5 == 0 and i % 3 != 0:
        print(i)
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print(i)
        print("FizzBuzz")
    else:  # is divisible by neither
        print(i)

# Opening a file
# make sure in correct directory
# pwd()

# cd ~

# %%

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv', 'rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        if line[1] == 'Total National Population':
#           print(line[0] + " " + line[5])  # numbers in column 6 - line[5] - are strings
            print("%s %s %s" % (line[0], line[5], type(line[5])))

# header = header.rstrip().split(',')
# header[5]

# %%
import collections

population_dict = collections.defaultdict(int)  # - cannot get line to work, even if import collections first
with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv', 'rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])  # turn string representation of population to integer
        if line[1] == 'Total National Population':
            population_dict[line[0]] += line[5]  # sums the two population values from the 2 records for the same country (rural and urban)
       
# %%  ALTERNATE WAY TO ACCOMPLISH THE SAME THING AS CODE DIRECTLY ABOVE
# one way to define the population_dict
from collections import defaultdict
population_dict = defaultdict(int)     

# Yet another way to open and read a file - need to close it at the end
inputFile = open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv', 'r')
header = next(inputFile)
for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])  # turn string representation of population to integer
        if line[1] == 'Total National Population':
            population_dict[line[0]] += line[5]  # sums the two population values from the 2 records for the same country (rural and urban)
inputFile.close()
# at point I thought they told us not to use the inputFile.close(), but to use the with open() as inputFile:

# %%  Write the data to a file
with open('national_population.csv', 'w') as outputFile:
    outputFile.write('continent,2010_population\n')
    for k, v in population_dict.iteritems():
        outputFile.write(k + ',' + str(v) + '\n')
        
# %% 
'''The data world is now your oyster. Play with some of the other population data and see what you come up with. Try and calculate the population change between 2010 and 2100. Remember the lesson about doing integer division. Convert one of the numbers to floating point decimal by using the float() function. Which continent is estimated to grow the most in the next 90 years?
Try and calculate the population density (total national population divided by the total land area and remember to convert at least one number to float). Which continent was most densely populated in 2010?'''

# %%
with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv','rU') as inputFile:
    for line in inputFile:
        line = line.rstrip().split(',')
        print(line)
        
# %%
with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv','rU') as inputFile:
    for line in inputFile:
        line = line.rstrip().split(',')
        print(len(line))

# %%
'''The len() function counts different things depending on what it's called on. If it's called on a list as in this example, it counts the number of elements in the list, not the length of the elements themselves. If len() is called on a string, it will count the number of characters in the string. This can be useful when iterating through a list, though most times it's unnecessary. The method we've been using (for i in list:) will iterate through the list and access the elements. An alternative that produces the same result would be to use:'''

# need to define my_list first
for i in range(len(my_list)): 
    print(my_list[i])
    
# %% USINE CSV PACKAGE
import csv

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv','r') as inputFile:
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        print(line)
        
# %%
with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv','r') as inputFile:
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        print(len(line))
        
# %% PANDAS!!
        
import pandas as pd

input_dataframe = pd.read_csv('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv')

# %%

input_dataframe['Continent']  # Writes the 'Continent' column of all rows to the screen

# %%
input_dataframe[0:10] # Writes just the first 10 rows of the data frame (showing all columns) to the console
