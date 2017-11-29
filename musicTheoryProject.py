# -*- coding: utf-8 -*-
"""
Vikram Amin
vamin@hmc.edu
Oct 27, 2017
"""

import pandas as pd
import re

df=pd.read_csv("//Users/TheMusician/Desktop/PitchClassGroups.csv")

#df['Vector']=df['Vector'].apply(lambda x: x.rstrip("0"))

#takes in string converts to array of ints
search_string = input('Enter search: ')



def pitches_input(pitchClassesString,df):
    pitchClassesString+=','
    start=0
    stop=0
    pitchClasses=pd.Series()
    for i in range(len(pitchClassesString)):
        if pitchClassesString[i]==',':
            stop=i
            pitchClasses=pitchClasses.append(pd.Series(int(pitchClassesString[start:stop])))
            start=i+1
    
    #reindexing
    pitchClasses.index = range(len(pitchClasses))
    
    
    print(pitchClasses)
    
    #builds vector
    vector_diff=pd.Series()
    
    for i in range(len(pitchClasses)):
        for j in range(len(pitchClasses)-i-1):
            vector_diff=vector_diff.append(pd.Series(abs(pitchClasses[i]-pitchClasses[i+j+1])))
    
    vector_diff.index = range(len(vector_diff))
            
    print(vector_diff)
    
    
    
    for i in range(len(vector_diff)):
        if (vector_diff[i]>6):
            vector_diff[i]=12-vector_diff[i]
    
    one_of_each=pd.Series(range(1,7))
    
    vector_diff=vector_diff.append(one_of_each)
    
    vector=vector_diff.value_counts()
    vector -= 1
    
    vector=vector.sort_index()
    print(vector)
    
    vector_as_string=vector.to_string(index=False)
    vector_as_string=re.sub("\D", "", vector_as_string)
    vector_as_string=vector_as_string.lstrip('0')
    #print(vector_as_string)
    input_set_df=df.loc[df['Vector'] == vector_as_string]
    print(input_set_df)


if(',' in search_string):
    pitches_input(search_string,df)
else:
    matched_search_df=df.loc[df['Vector'] == search_string]
    print(matched_search_df)
    matched_search_df=df.loc[df['Set Name'] == search_string]
    print(matched_search_df)
    matched_search_df=df.loc[df['Prime Form'] == search_string]
    print(matched_search_df)
    matched_search_df=df.loc[df['Description'] == search_string]
    print(matched_search_df)


def vector_add(vector1,vector2):
    summed_vector=''
    for i in range(len(vector1)):
        summed_vector+=str( int( vector1[i] ) + int( vector2[i] ) )
    
    return summed_vector
    
    
def find_subsets(given_vector):
    two_additions_df=pd.DataFrame(columns=('Set1', 'Set2', 'Vector1','Vector2','Combined Vector'))
    for index1, row1 in df.iterrows():
        for index2, row2 in df.iterrows():
            set1=row1['Set Name']
            vector1=row1['Vector']
            set2=row2['Set Name']
            vector2=row2['Vector']
            summed_vector=vector_add(vector1,vector2)
            two_additions_df.loc[index1+index2] = [set1,set2,vector1,vector2,summed_vector]
    
    matched_search_df=df.loc[df['Combined Vector'] == given_vector]
    print(matched_search_df)
    
    
    
    
