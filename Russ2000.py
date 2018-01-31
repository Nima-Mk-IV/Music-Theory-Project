# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:24:39 2018
Russ 2000
@author: aminv
"""

import pandas as pd #how to get pandas into a given document once installed will now be called pd

#####################
#How to make a dataframe
#####################
d = {'col1': [1, 2], 'col2': [3, 4]} #data to put into dataframe
df = pd.DataFrame(data=d) #putting the data into a dataframe so we can now use pandas functionality

df=pd.read_csv("document address") #how to read a excel sheet into pandas, first must export sheet as csv

#####################
#How to subset a dataframe
#####################
sub_df=df['col1']#gives col1

sub_df2=df.iloc[[2]]#gives row 2

sub_df3=df.iloc[[2:3]]#gives row 2-3


#####################
#How to get information about a dataframe
#####################

df.shape #returns a tuple (# rows, # cols)
df.head(5) #returns the first 5 rows
df.describe() #gives you statistics on every col

#####################
#How to modify a dataframe
#####################

df['col1'].apply(lambda x: f(x)) #will apply f to every element in col1 can call on the entire dataframe too

#iterating through a dataframe:
for index, row in df.iterrows():
    do x,y,z
    