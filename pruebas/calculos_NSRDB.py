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


#
def sb_calculate(row):
    if int(row) > 120:
        return 1.0
    else:
        return 0.0
#

def monthly_trapezoid_average(dataset_filtered):
    
    #
    dataset_filtered = dataset_filtered.drop(['DHI', 'DNI'], axis=1)
    #
    dataset_filtered['Date'] = pd.to_datetime(dataset_filtered['Date'])

    dataset_filtered.set_index('Date', inplace=True)
    
    df_daily = dataset_filtered.resample('D').apply(lambda x: (x[:-1] + x[1:]) / 2)
    
    #
    df_daily['SB_GHI'] = df_daily['GHI'].apply(sb_calculate)
    #
    
    #print(df_daily.head(30))
    df_daily.to_csv(filtered_folder + year + '/' + year + '_days.csv')
    monthly_dataset = pd.read_csv(filtered_folder + year + '/' + year + '_days.csv')
    os.remove(filtered_folder + year + '/' + year + '_days.csv')
    monthly_dataset = monthly_dataset.drop(['Date.1', 'Hour'], axis=1)
    
    monthly_dataset['Date'] = pd.to_datetime(monthly_dataset['Date'])
    monthly_dataset.set_index('Date', inplace=True)
    #print(monthly_dataset.head(30))
    
    ### cambio de lugar la std
    #
    monthly_sum = monthly_dataset['GHI'].resample('M').transform('sum')
    monthly_avg = monthly_dataset['SB_GHI'].resample('D').transform('sum')
    
    monthly_sum = pd.concat([monthly_sum, monthly_avg], axis=1)
    
    #print(monthly_sum.head(30))

    #monthly_average
    #
    
    std_dataset = monthly_dataset.resample('M').transform('std')
    std_dataset = std_dataset.rename(columns=lambda x: 'std ' + x)
    
    
    daily_final_sum = pd.concat([monthly_sum, std_dataset], axis=1)
    daily_final_sum = daily_final_sum.resample('M').mean()
    daily_final_sum.reset_index(inplace=True)

    #print(daily_final_sum.head(30))
    return daily_final_sum

def units_solar(df):
    df['Date'] = pd.to_datetime(df['Date'])

    # Crear una nueva columna 'dia' con el número del día correspondiente a cada fecha
    df['dias_mes'] = df['Date'].dt.day
    
    # Multiplicar cada columna del dataframe, excepto la columna 'Date', por 1000*dia
    #df.iloc[:, 1:] = df.iloc[:, 1:].apply(lambda x: x / (1000 * df['dias_mes']))
    df.iloc[:, 1:3] = df.iloc[:, 1:3].apply(lambda x: x / (1000 * df['dias_mes']))
    
    df = df.drop('dias_mes', axis=1)
    
    return df

working_directory = 'C:/Users/seforeros/OneDrive/Escritorio/proyectos/renewable/pruebas/' #cambiar
years_folder = working_directory + 'csv_clara/' #cambiar
filtered_folder = working_directory + 'csv_filtered/' #cambiar

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
        #solar_daily = solar_daily[['Date', 'GHI', 'std GHI', 'DHI', 'std DHI', 'DNI', 'std DNI']]
        solar_daily = solar_daily[['Date', 'GHI', 'std GHI', 'SB_GHI', 'std SB_GHI']]
        solar_monthly = units_solar(solar_daily)
        anual_data = pd.concat([solar_monthly, wind_monthly], axis=1)
        anual_data.insert(1, 'Longitude', info[0])
        anual_data.insert(2, 'Latitude', info[1])
        anual_data.insert(3, 'Elevation', info[2])
        
        anual_data.to_csv(filtered_folder + year + '/' + filename[7:20] + '.csv')
    
    #print(f'Year {year} successfully processed')
    print(f'Jahr {year} erfolgreich bearbeitet')