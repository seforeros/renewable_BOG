# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 23:59:20 2023

@author: seforeros
"""

import pandas as pd
import os

working_directory = 'C:/Users/seforeros/OneDrive/Escritorio/proyectos/renewable/pruebas/' #cambiar
years_folder = working_directory + 'data_calculated/' #cambiar
report_folder_solar = working_directory + 'data_report/solar/' #cambiar
report_folder_wind = working_directory + 'data_report/wind/' #cambiar

years = ['1998', '1999']

files_total = os.listdir(years_folder + years[0])

df_point_multianual = pd.DataFrame() # df que guarda los promedios multianuales para cada putno

for file in files_total:
    
    df_point_total = pd.DataFrame() # df que guarda todos los datos temporales para un unico punto
    
    for year in years:
        
        df = pd.read_csv( years_folder + year + '/' + file)
        df_point_total = pd.concat([df_point_total, df], ignore_index = False) # agrego todos los años
        
    df_point_total['Date'] = pd.to_datetime(df_point_total['Date'])
    df_point_total['Month'] = df_point_total['Date'].dt.month
    #df_point_total = df_point_total.drop('Date', axis=1)
    df_point_total['Date'] = pd.to_datetime('01/' + df_point_total['Month'].astype(str) + '/2000', format='%d/%m/%Y')
    df_point_total['Date'] = pd.to_datetime(df_point_total['Date'])
    df_point_total.set_index('Date', inplace=True)
    
    df_point_total = df_point_total.resample('M').mean() # promedio por cada mes
    df_point_total.reset_index(inplace=True)
    df_point_total = df_point_total.drop(['Date', 'Unnamed: 0'], axis=1)
    
    df_point_multianual = pd.concat([df_point_multianual, df_point_total], ignore_index = False)
    
    print(f'Punkt {file} erfolgreich bearbeitet')     
df_point_multianual.to_csv(report_folder_solar + '/multianual_prueba.csv')