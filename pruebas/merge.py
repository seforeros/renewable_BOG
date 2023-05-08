# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 18:10:33 2023

@author: seforeros
"""

import pandas as pd
import os

working_directory = 'C:/Users/seforeros/OneDrive/Escritorio/proyectos/renewable/pruebas/' #cambiar
filtered_folder = working_directory + 'csv_filtered/' #cambiar
report_folder = working_directory + 'data_report/'   #cambiar

years = ['1998', '1999']

df = pd.DataFrame()

for year in years:

    for filename in os.listdir(filtered_folder + year):
        
        df_year = pd.read_csv(filtered_folder + year + '/' + filename)
        
        df = pd.concat([df, df_year], ignore_index = False)

df = df.drop(df.columns[[0, 7, 8, 9, 10]], axis=1)
df.to_csv(report_folder + 'data_merged.csv')