import pandas as pd
import os

local_storage_directory = 'C:/Users/seforeros/OneDrive/Escritorio/proyectos/renewable/pruebas/'
csv_dir = local_storage_directory + 'csv_clara/'
filtered_dir = local_storage_directory + 'csv_filtered/'

files_to_convert = csv_dir

lon_min = -74.638
lat_min = 3.571
lon_max = -73.710
lat_max = 5.057

for filename in os.listdir(files_to_convert):
    df = pd.read_csv(files_to_convert + filename)
    filtered_df = df[(df['lat'] >= lat_min) & (df['lat'] <= lat_max) & (df['lon'] >= lon_min) & (df['lon'] <= lon_max)]
    filtered_df.to_csv(filtered_dir + filename[:-3] + '.csv')
    print(filename + ' has been filtered into the area')
