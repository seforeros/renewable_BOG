# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:53:28 2023

@author: seforeros
"""
import pandas as pd
import os

local_storage_directory = 'D:/pqr_ideam/'
data_dir = local_storage_directory + 'datos_viento_data/'
csv_dir = local_storage_directory + 'datos_viento_csv/'

folders_to_convert = data_dir

for foldername in os.listdir(folders_to_convert):
    for filename in os.listdir(folders_to_convert + foldername):
        #print(foldername+' ---> '+filename) 
    
        # Carga el archivo .data en un DataFrame de pandas
        df = pd.read_csv(folders_to_convert + foldername + '/' + filename, sep=" ")
        
        # Convertir el índice en una columna
        df = df.reset_index()

        #utilizar la función rename()
        df.columns = ['fecha'] + list(df.columns[1:])
        
        # Dividir la columna en dos columnas
        df[['hora', 'valor']] = df['Fecha|Valor'].str.split('|', expand=True)
        
        #elimino columnas que no sirven
        df = df.drop('Fecha|Valor', axis=1)
        df = df.drop('hora', axis=1)
        
        df.to_csv(csv_dir + foldername + '/' + filename[:-5] + '.csv')
        print(foldername + '/' + filename + ': has been processed to .csv')