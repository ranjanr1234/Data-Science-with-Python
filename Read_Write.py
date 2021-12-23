# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 18:11:32 2021

@author: Rajeev
"""


import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('D:/skill edge/User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('D:/skill edge/IIT-B.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('D:/skill edge/User_Data.xlsx')

df1 = pandas.read_excel('User_Data.xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('IIT-B.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)