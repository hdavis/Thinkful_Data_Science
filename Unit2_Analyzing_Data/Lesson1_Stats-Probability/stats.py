# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 11:02:51 2016

@author: Holly
"""

import pandas as pd
import scipy.stats as stats

# data source: http://lib.stat.cmu.edu/DASL/Datafiles/AlcoholandTobacco.html
data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

# split string on the hidden characters that indicate new lines
data = data.splitlines()

# Split each item in this list on the commas; the bracketed expression is a list comprehension. Converts the 'data' list to a list of lists (each row or region becomes a list instead of a string)
data = [i.split(',') for i in data]

column_names = data[0] # data[0] is the first list item in the data list and will become the column names.
data_rows = data[1::] # data[1::] are the second and all following list items within the data list which will become the rows of data in the dataframe
df = pd.DataFrame(data_rows, columns=column_names)

# note data are all strings, including numeric values.  Will need to convert to float.
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

# calc Alcohol stats
mean_Alcohol = df['Alcohol'].mean()
median_Alcohol = df['Alcohol'].median()
mode_Alcohol = stats.mode(df['Alcohol'])
range_Alcohol = df['Alcohol'].max() - df['Alcohol'].min() # one way to calc range
range_Alcohol2 = max(df['Alcohol']) - min(df['Alcohol']) # another way to calc range
std_Alcohol = df['Alcohol'].std()
var_Alcohol = df['Alcohol'].var()

# calc Tobacco stats
mean_Tobacco = df['Tobacco'].mean()
median_Tobacco = df['Tobacco'].median()
mode_Tobacco = stats.mode(df['Tobacco'])
range_Tobacco = df['Tobacco'].max() - df['Tobacco'].min() # one way to calc range
range_Tobacco2 = max(df['Tobacco']) - min(df['Tobacco']) # another way to calc range
std_Tobacco = df['Tobacco'].std()
var_Tobacco = df['Tobacco'].var()

print('The following are the summary statistics for the weekly household spending data in the Alcohol and Tobacco dataset. All values are in British pounds spent per week in 1981.')
print('\n')
print('The mean for Alcohol is {:.2f} pounds.'.format(mean_Alcohol))
print('The median for Alcohol is {} pounds.'.format(median_Alcohol))
print('The mode for Alcohol is {} pounds.'.format(mode_Alcohol[0][0]))
print('The range for Alcohol is {} pounds.'.format(range_Alcohol))
print('The standard deviation for Alcohol is {:.3f} pounds.'.format(std_Alcohol))
print('The variance for Alcohol is {:.3f} pounds.'.format(var_Alcohol))
print('\n')
print('The mean for Tobacco is {:.2f} pounds.'.format(mean_Tobacco))
print('The median for Tobacco is {} pounds.'.format(median_Tobacco))
print('The mode for Tobacco is {} pounds.'.format(mode_Tobacco[0][0]))
print('The range for Tobacco is {} pounds.'.format(range_Tobacco))
print('The standard deviation for Tobacco is {:.3f} pounds.'.format(std_Tobacco))
print('The variance for Tobacco is {:.3f} pounds.'.format(var_Tobacco))

df.to_csv('vice.csv', index=False)
