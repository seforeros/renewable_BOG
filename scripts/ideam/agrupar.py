# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 07:35:18 2023

@author: seforeros
"""
import os
import shutil

# velocidad
#local_storage_directory = 'D:/pqr_ideam/datos_viento_csv/vel_viento/'
#final_directory = 'D:/pqr_ideam/velocidad'

# direccion
local_storage_directory = 'D:/pqr_ideam/datos_viento_csv/direccion_viento/'
final_directory = 'D:/pqr_ideam/direccion_viento'

# Obtener la lista de nombres de archivos
nombres_archivos = os.listdir(local_storage_directory)

for filename in os.listdir(local_storage_directory):
    
    for file in nombres_archivos:

        if file[-12:-4] == filename[-12:-4]:
            
            try:
                # Ruta completa del archivo a mover
                ruta_archivo = os.path.join(local_storage_directory, file)
                
                # Crear la carpeta si no existe
                if not os.path.exists(final_directory + '/' + filename[-12:-4]):
                    os.makedirs(final_directory + '/' + filename[-12:-4])
                
                # Mover el archivo a la carpeta destino            
                shutil.move(ruta_archivo, final_directory + '/' + filename[-12:-4])
            except:
                print("An exception occurred")

        print('Archivo: '+ file + ' movido')