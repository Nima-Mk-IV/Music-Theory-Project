# -*- coding: utf-8 -*-
"""
Vikram Amin
vamin@hmc.edu
Oct 27, 2017
"""

import pandas as pd
import re

#Pitch Class Set data
df=pd.read_csv("C:/Users/aminv/Desktop/Music-Theory-Project-master/Music-Theory-Project-master/PitchClassGroups.csv")
df['Vector']=df['Vector'].astype(str)
df['Vector']=df['Vector'].apply(lambda x: x.rstrip("0"))

#takes in string converts to array of ints
search_string = str(input('Enter search: '))


#deals with finding vector form if pitches are inputted
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




#helper function for adding these types of 'vectors'
def vector_add(vector1,vector2):
    while(len(vector1)<len(vector2)):
        vector1+='0'
    while(len(vector2)<len(vector1)):
        vector2+='0'
    summed_vector=''
    for i in range(len(vector1)):
        summed_vector+=str( int( vector1[i] ) + int( vector2[i] ) )
    summed_vector.rstrip("0")
    return summed_vector
    
#builds the dictionary of all two combinations
def create_two_additions():
    two_additions_df=pd.DataFrame(columns=('Set1', 'Set2', 'Vector1','Vector2','Combined Vector'))
    for index1, row1 in df.iterrows():
        for index2, row2 in df.iterrows():
            set1=row1['Set Name']
            vector1=row1['Vector']
            set2=row2['Set Name']
            vector2=row2['Vector']
            summed_vector=vector_add(vector1,vector2)
            two_additions_df.loc[len(two_additions_df)]=[set1,set2,vector1,vector2,summed_vector]
    two_additions_df=two_additions_df.drop_duplicates()
    two_additions_df['Combined Vector']=two_additions_df['Combined Vector'].apply(lambda x: x.rstrip("0"))
    two_additions_df.to_pickle("C:/Users/aminv/Desktop/Music-Theory-Project-master/Music-Theory-Project-master/two_additions_df.pkl")

#builds the dictionary of all 3 combinations
def create_three_additions():
    three_additions_df=pd.DataFrame(columns=('Set1', 'Set2', 'Set3', 'Vector1','Vector2','Vector3','Combined Vector'))
    for index1, row1 in df.iterrows():
        for index2, row2 in df.iterrows():
            for index3, row3 in df.iterrows():
                set1=row1['Set Name']
                vector1=row1['Vector']
                set2=row2['Set Name']
                vector2=row2['Vector']
                set3=row3['Set Name']
                vector3=row3['Vector']
                summed_vector=vector_add(vector1,vector2)
                summed_vector=vector_add(summed_vector,vector3)
                three_additions_df.loc[index1+index2] = [set1,set2,set3,vector1,vector2,vector3,summed_vector]
    three_additions_df=three_additions_df.drop_duplicates()
    three_additions_df['Combined Vector']=three_additions_df['Combined Vector'].apply(lambda x: x.rstrip("0"))
    three_additions_df.to_pickle("C:/Users/aminv/Desktop/Music-Theory-Project-master/Music-Theory-Project-master/three_additions_df.pkl")

#finds sets which add to a given set inputted in vector form
def find_subsets(given_vector):
    two_additions_df=pd.read_pickle("C:/Users/aminv/Desktop/Music-Theory-Project-master/Music-Theory-Project-master/two_additions_df.pkl")
    three_additions_df=pd.read_pickle("C:/Users/aminv/Desktop/Music-Theory-Project-master/Music-Theory-Project-master/three_additions_df.pkl")

    print('Combinations of 2 Sets:')
    matched_search_df=two_additions_df.loc[two_additions_df['Combined Vector'] == given_vector]
    print(matched_search_df)
    
    print('Combinations of 3 Sets:')
    matched_search_df=three_additions_df.loc[three_additions_df['Combined Vector'] == given_vector]
    print(matched_search_df)
    
    
if(',' in search_string):
    print('Information About Input:')
    pitches_input(search_string,df)
else:
    print('Information About Input:')
    print(matched_search_df)


    
