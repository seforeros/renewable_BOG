# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 17:24:22 2023

@author: seforeros
"""

import pandas as pd
import math
import os

working_directory = 'C:/Users/seforeros/OneDrive/Escritorio/proyectos/renewable/pruebas/' #cambiar
years_folder = working_directory + 'csv_filtered/' #cambiar
final_folder = working_directory + 'data_calculated/'   #cambiar

years = ['1998', '1999']


def temp_80m(row, h = 80):
    
    # T en grados C
    T_80 = row + (-6.5*(h/1000))
    
    return T_80

def calcular_presion_80m(row):
    # Obtener los valores de presión, temperatura y velocidad del viento
    p0 = row['Pressure']
    t0 = row['T 80m'] + 273.15  # Convertir a kelvin
    
    R = 8.31432 # N m / mol K # Es la constante universal del gas
    g = 9.80665 # m/s2 # Es la aceleración gravitacional
    M = 0.0289645 # kg/mol # Es la Masa molar del aire de la tierra
    h = 80
    
    # Calcular la presión a 80m
    P_80m = p0 * math.exp(-(M * g * h)/(R * (t0)))
    
    # Devolver la presión a 80m
    return P_80m

def rho_80m(row):
    
    p0 = row['P 80m']*1000 # convertir a Pa
    t0 = row['T 80m'] + 273.15  # Convertir a kelvin
    
    R = 8.31432 # N m / mol K # Es la constante universal del gas
    M = 0.0289645 # kg/mol # Es la Masa molar del aire de la tierra
    
    rho_80m = (M * p0)/(R * t0)
    
    return rho_80m

def rho_PE_80m(row):
    
    Cp = 0.59  # factor de perdidas
    rho_h = row['rho 80m'] # convertir a Pa
    vel = row['vel 80m']  # Convertir a kelvin
    
    rho_PE = Cp*(1/2)*rho_h*(vel**3)
    
    return rho_PE
    
h = 80
alpha = 0.25

for year in years:

    for filename in os.listdir(years_folder + year):
        
        df = pd.read_csv( years_folder + year + '/' + filename )
        
        #df = df.loc[:, ['Date', 'Longitude', 'Latitude', 'Elevation', 'Wind Speed', 'std Wind Speed', 'Wind Direction', 'std Wind Direction', 'Temperature', 'std Temperature', 'Pressure', 'std Pressure']]
        
        df['Pressure'] = df['Pressure']/10 # correccion de mbar a kPa
        df['std Pressure'] = df['std Pressure']/10
        df['T 80m'] = df['Temperature'].apply(temp_80m)
        df['P 80m'] = df.apply(calcular_presion_80m, axis=1)
        df['vel 80m'] = df['Wind Speed'] * (h/10)**alpha
        df['rho 80m'] = df.apply(rho_80m, axis=1)
        df['rho_PE 80m'] = df.apply(rho_PE_80m, axis=1)
        
        #df = df.loc[:, ['Date', 'Longitude', 'Latitude', 'Elevation', 'Wind Speed', 'std Wind Speed', 'Wind Direction', 'std Wind Direction', 'rho_PE 80m']]
        df = df.drop('Unnamed: 0', axis=1)
        df.to_csv( final_folder + year + '/' + filename)
    
    print(f'Jahr {year} erfolgreich bearbeitet')