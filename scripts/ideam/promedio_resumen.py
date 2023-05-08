# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 08:06:17 2023

@author: seforeros
"""
import os 
import pandas as pd

# calculo de lo promedios mensuales
def monthly_average(dataset_filtered):
    
    dataset_filtered['fecha'] = pd.to_datetime(dataset_filtered['fecha'])
    dataset_filtered.set_index('fecha', inplace=True)
    
    std_dataset = dataset_filtered.resample('M').std()
    std_dataset = std_dataset.rename(columns=lambda x: 'std ' + x)
    avg_dataset = dataset_filtered.resample('M').mean()

    monthly_dataset = pd.concat([avg_dataset, std_dataset], axis=1)
    monthly_dataset.reset_index(inplace=True)

    return monthly_dataset

# Definir una función para obtener la fecha más temprana y la fecha más reciente
def obtener_rango_fechas(dataframe, columna_fechas):
    fecha_min = dataframe[columna_fechas].min()
    fecha_max = dataframe[columna_fechas].max()
    return fecha_min, fecha_max

#------------------------------------------------------------------------------

# velocidad
local_directory = 'D:/pqr_ideam/velocidad/'

# direccion
#local_directory = 'D:/pqr_ideam/direccion_viento/'

df_CNI = pd.read_csv('CNE_IDEAM.csv', encoding='latin1')

points = os.listdir(local_directory)

df_total = pd.DataFrame()

for folder in points:
    df_point = pd.DataFrame()
    
    for filename in os.listdir(local_directory + folder):
        
        if filename != 'resumen.csv':
            df = pd.read_csv(local_directory + folder + '/' + filename)
        
            nombre_variable = filename.split('@')[0]
            promedio = df['valor'].mean()
            #lat, lon = obtener_latlon(df_CNI, folder)
            lat = df_CNI[df_CNI['CODIGO'] == int(folder)]['latitud']
            lon = df_CNI[df_CNI['CODIGO'] == int(folder)]['longitud']
            fecha_min, fecha_max = obtener_rango_fechas(df, 'fecha')
            
            datos_dataframe = {
                'variable': nombre_variable,
                'promedio': promedio,
                'estacion': folder,
                'latitud': lat,
                'longitud': lon,
                'fecha_min': fecha_min,
                'fecha_max': fecha_max
                }
        
            df_file = pd.DataFrame(datos_dataframe)
        
        try:
            # Concatenar los DataFrames
            df_point = pd.concat([df_point, df_file])
        except:
            print('archivo de resumen')
            
        print('archivo procesado exitosamente')
    
    df_point.to_csv(local_directory + folder + '/resumen.csv')
    
    # guardar el resumen para todos los datos
    df_total = pd.concat([df_total, df_point])
    
df_total.to_csv(local_directory + 'resumen_puntos.csv')