import numpy as np
import pandas as pd
import os

def adjust_df(dataframes_location):

    coordinates = pd.read_csv(dataframes_location, nrows=1)
    df = pd.read_csv(dataframes_location, skiprows=2)

    df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
    df = df.drop(['Year', 'Month', 'Day', 'Minute'], axis=1)
    df = df[['Date','Hour','Wind Speed','Wind Direction','Temperature','Pressure','GHI','DHI','DNI']]

    inf = [coordinates['Longitude'][0], coordinates['Latitude'][0], coordinates['Elevation'][0]]
    df2 = df.loc[:, ['Date', 'Wind Speed', 'Wind Direction', 'Temperature', 'Pressure']]
    df3 = df.loc[:, ['Date', 'Hour', 'GHI', 'DHI', 'DNI']]

    return inf, df2, df3

def monthly_average(dataset_filtered):
    
    
    dataset_filtered['Date'] = pd.to_datetime(dataset_filtered['Date'])
    dataset_filtered.set_index('Date', inplace=True)
    
    std_dataset = dataset_filtered.resample('M').std()
    std_dataset = std_dataset.rename(columns=lambda x: 'std ' + x)
    avg_dataset = dataset_filtered.resample('M').mean()

    monthly_dataset = pd.concat([avg_dataset, std_dataset], axis=1)
    monthly_dataset.reset_index(inplace=True)

    return monthly_dataset

def monthly_trapezoid_average(dataset_filtered):
    
    dataset_filtered['Date'] = pd.to_datetime(dataset_filtered['Date'])
    dataset_filtered.set_index('Date', inplace=True)
    
    df_daily = dataset_filtered.resample('D').apply(lambda x: (x[:-1] + x[1:]) / 2)
    
    df_daily.to_csv(filtered_folder + year + '/' + year + '_days.csv')
    monthly_dataset = pd.read_csv(filtered_folder + year + '/' + year + '_days.csv')
    os.remove(filtered_folder + year + '/' + year + '_days.csv')
    monthly_dataset = monthly_dataset.drop(['Date.1', 'Hour'], axis=1)
    monthly_dataset['Date'] = pd.to_datetime(monthly_dataset['Date'])
    monthly_dataset.set_index('Date', inplace=True)
    
    monthly_dataset = monthly_dataset.resample('D').transform('sum')
    monthly_dataset.reset_index(inplace=True)

    return monthly_dataset


working_directory = 'C:/Users/seforeros/OneDrive/Escritorio/proyectos/renewable/pruebas/' #cambiar
years_folder = working_directory + 'csv_clara/' #cambiar
filtered_folder = working_directory + 'csv_filtered/'   #cambiar

years = ['1998', '1999']

for year in years:

    for filename in os.listdir(years_folder + year):

        info, wind, solar = adjust_df( years_folder + year + '/' + filename )

        # viento -----------------------------------------------------------------------------------------

        wind_monthly = monthly_average(wind)
        wind_monthly = wind_monthly[['Wind Speed','std Wind Speed','Wind Direction','std Wind Direction',
                                     'Temperature','std Temperature','Pressure','std Pressure']]

        # solar  ------------------------------------------------------------------------------------------
        
        solar_daily = monthly_trapezoid_average(solar)
        
        solar_monthly = monthly_average(solar_daily)
        solar_monthly = solar_monthly[['Date', 'GHI', 'std GHI', 'DHI', 'std DHI', 'DNI', 'std DNI']]
        
        anual_data = pd.concat([solar_monthly, wind_monthly], axis=1)
        anual_data.insert(1, 'Longitude', info[0])
        anual_data.insert(2, 'Latitude', info[1])
        anual_data.insert(3, 'Elevation', info[2])
        
        anual_data.to_csv(filtered_folder + year + '/' + year + '.csv')
        
        
        

        

        
        