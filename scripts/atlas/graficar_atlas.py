# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 19:20:02 2023

@author: seforeros
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
# Carga el archivo CSV con las coordenadas de latitud
latitud = pd.read_csv('Latitudes.csv', header=None)

# Carga el archivo CSV con las coordenadas de longitud
longitud = pd.read_csv('Longitudes.csv', header=None)

# Carga el archivo CSV con los valores de densidad de aire
densidad = pd.read_csv('RadGlobal.csv', header=None)


# Aplana los vectores de coordenadas de latitud y longitud
x = longitud.values.flatten()
y = latitud.values.flatten()

# Grafica el scatter
plt.scatter(x, y, c=densidad.values)
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.colorbar(label='Radiacion')
plt.show()

'''

# Carga los datos desde los archivos CSV
latitud = np.loadtxt('Latitudes.csv', delimiter=',')
longitud = np.loadtxt('Longitudes.csv', delimiter=',')
densidad = np.loadtxt('RadGlobal.csv', delimiter=',')

# Crea una malla de coordenadas a partir de los vectores de latitud y longitud
longitud, latitud = np.meshgrid(longitud, latitud)


fig, ax = plt.subplots(figsize = (8,10))
im = plt.scatter(longitud, latitud, c=densidad, marker='s', s = 8)

ax.set_title('el yamba me lo pela')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.xlim = ([min(longitud).any(), max(longitud).any()])
ax.ylim = ([min(latitud).any(), max(latitud).any()])
fig.colorbar(im, ax=ax)
ax.axis('equal')

# Muestra la gráfica
plt.show()