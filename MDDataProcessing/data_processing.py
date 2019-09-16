# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 22:11:00 2019

@author: Marisa Elena Gonzalez 

"""
import pandas as pd
#import numpy as np
#import utilityfunctions as uf
#import matplotlib.pyplot as plt

#turn into ONE function
def parseRawDataToCSV(filename):
    lines = []
    
    with open(filename) as f:
        lines = f.readlines()
        
    timestamps = []
    
    #create Empty Lists
    t_times = []
    t_list = []
    
    c_times = []
    c_list = []
    
    s_times = []
    s_list = []
    
    #sort things
    current_timestamp = ''
    for line in lines:
        if line[0].isdigit():
            current_timestamp = line.rstrip()
            timestamps.append(current_timestamp)
            continue
        if line[0] == 'T':
            t_times.append(current_timestamp)
            t_list.append(line.rstrip()[2:].lstrip())
            continue
        if line[0] == 'C':
            c_times.append(current_timestamp)
            c_list.append(line.rstrip()[2:].lstrip())
            continue
        if line[0] == 'S':
            s_times.append(current_timestamp)
            s_list.append(line.rstrip()[2:].lstrip())
            continue
    
    
    t_df = pd.DataFrame(
            list(
                    zip(
                            t_times,
                            t_list)
                    ),
                    columns = [
                            'Timestamp',
                            'Temperature'
                            ]
                    )     
    c_df = pd.DataFrame(
            list(
                    zip(
                            c_times,
                            c_list
                            )
                    ),
                    columns = [
                            'Timestamp',
                            'Conductivity'
                            ]
                    )  
    s_df = pd.DataFrame(
            list(
                    zip(
                            s_times,
                            s_list
                            )
                    ),
                    columns = [
                            'Timestamp',
                            'Scale'
                            ]
                    )  
    
    #seperating temperature columns
    t_df[
            [
                    'Temperature1',
                    'Temperature2',
                    'Temperature3',
                    'Temperature4',
                    'T Since Start'
                    ]
            ] = t_df.Temperature.str.split(',', expand = True) 
#    t_df[['Timestamp', 'Temperature1', 'Temperature2', 'Temperature3', 'Temperature4', 'Since Start']]
    
    #seperating conductivity columns 
    c_df[
            [
                    'Conductivity',
                    'C Since Start' 
                    ]
            ] = c_df.Conductivity.str.split(',', expand = True) 
    
    #seperating scale columns 
    temp_string = s_df['Scale'].str.replace('\?','').str.replace('NET','').str.replace('\s+',' ')
    temp_df = temp_string.str.split(' ',expand=True)
    s_df['Weight'] = temp_df[0]
    s_df['Unit'] = temp_df[1]
    s_df['S Since Start'] = temp_df[2]
    s_df.drop('Scale', inplace=True, axis=1)
#    s_df = s_df.drop(, axis=1)
#    print(s_df.keys())
#    s_df[['Weight', 'Unit', 'Since Start']]
    
    
    #send temperature, conductivity, and scale data to csv files  
    t_df.to_csv('temperature.csv')
    c_df.to_csv('conductivity.csv')
    s_df.to_csv('scale.csv')

filename = 'data.txt'
parseRawDataToCSV(filename)
# import CSV files back into pandas
t_df = pd.read_csv(
        'temperature.csv',
        index_col='Timestamp',
        header=0, 
        parse_dates=True
        )
c_df = pd.read_csv(
        'conductivity.csv', 
        index_col='Timestamp', 
        header=0,
        parse_dates=True
        )
s_df = pd.read_csv(
       'scale.csv', 
       index_col='Timestamp', 
       header=0,
       parse_dates=True
       )

# remove index column 
s_df.drop(columns='Unnamed: 0', inplace=True)
t_df.drop(columns='Unnamed: 0', inplace=True)
c_df.drop(columns='Unnamed: 0', inplace=True)

# change from string to time difference
s_df['S Since Start'] = pd.to_timedelta(s_df['S Since Start'])

# round index to nearest second
t_df['TS'] = t_df.index.round('S')
c_df['TS'] = c_df.index.round('S')
s_df['TS'] = s_df.index.round('S')

# delete duplicate timestamps 
t_df.drop_duplicates(
        subset='TS',
        keep='last',
        inplace=True
        )

c_df.drop_duplicates(
        subset='TS',
        keep='last',
        inplace=True
        )

s_df.drop_duplicates(
        subset='TS',
        keep='last',
        inplace=True
        )

# set the index in eacg dataframe to the rounded timestamps
t_df.set_index(
        keys='TS',
        drop=True,
        append=False,
        inplace=True
        )

c_df.set_index(
        keys='TS',
        drop=True,
        append=False,
        inplace=True
        )

s_df.set_index(
        keys='TS',
        drop=True,
        append=False,
        inplace=True
        )

#create one dataframe with ALL data
df = t_df.join(other=c_df, how='outer', sort=True, lsuffix='_t', rsuffix='_c')
df = df.join(other=s_df, how='outer', sort=True, rsuffix='_s')


# TODO: Find flux
# TODO: Graph!
# TODO: comment code





