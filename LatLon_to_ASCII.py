import rasterio
import numpy
import pandas as pd
from rasterio.transform import from_origin
df = pd.read_csv('output.csv')

# Define the latitude and longitude coordinates
latitude = df['Latitude'].tolist()
longitude = df['Longitude'].tolist()

# Define the cell size in degrees
cell_size = 0.04

# Define the nodata value
nodata = -9999

rows = 2000
columns = 3921

# Define the output file name
output_file = 'output_nsrdb.csv'

# Create the transformation matrix
transform = from_origin(min(longitude), max(latitude), cell_size, cell_size)

# Create the Esri ASCII grid data
#data_array
data_array = np.arange(1, rows*columns).reshape(rows, columns)

# Write the data to the output file
with rasterio.open(output_file, 'w', driver='AAIGrid', transform=transform, nodata=nodata, width=data_array.shape[1], height=data_array.shape[0], count=1, dtype=data_array.dtype) as dst:
    dst.write(data_array, 1)