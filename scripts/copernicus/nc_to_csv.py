import xarray as xr
import os

local_storage_directory = 'D:/data_copernicus/SRB/'
netcdf_dir = local_storage_directory + 'netcdf/'
csv_dir = local_storage_directory + 'csv/'

files_to_convert = netcdf_dir

for filename in os.listdir(files_to_convert):
    ds = xr.open_dataset(files_to_convert + filename)
    df = ds.to_dataframe()
    df.to_csv(csv_dir + filename[:-3] + '.csv')
    print(filename + ' has been processed to .csv')
