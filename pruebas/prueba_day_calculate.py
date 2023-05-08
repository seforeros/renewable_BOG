import numpy as np
import pandas as pd
import os

def calculate_day(dataframe_month, hours, df_day):

    df_model_day = pd.DataFrame(df_day)
    return_days = pd.DataFrame(df_day)

    days = np.arange(1, dataframe_month['Day'].max()+1)

    for day in days:
        filtered_day = dataframe_month.loc[dataframe_month['Day'] == day, :]
        #filtered_day = filtered_day.drop('Day', axis=1)

        for hour in hours:
            if hour == 0:
                row_hour = filtered_day.loc[filtered_day['Hour'] == hour]
                row_hour = row_hour.drop('Hour', axis=1)

                df_model_day = df_model_day.append(row_hour)  #iteracion anterior
                df_model_day = df_model_day.append(row_hour)  #acumulado

            elif hour == 1:
                row_hour_p = filtered_day.loc[filtered_day['Hour'] == hour]
                row_hour_p = row_hour_p.drop('Hour', axis=1)

                df_model_day.iloc[1, 5:12] = (df_model_day.iloc[0, 5:12] + row_hour_p.iloc[0, 5:12])/2

                df_model_day.iloc[0,:] = row_hour_p
                '''
            else:
                row_hour_p = filtered_day.loc[filtered_day['Hour'] == hour]
                row_hour_p = row_hour_p.drop('Hour', axis=1)

                df_model_day.iloc[1, 5:12] = df_model_day.iloc[1, 5:12] + (df_model_day.iloc[0, 5:12] + row_hour_p.iloc[0, 5:12]) / 2
                df_model_day[0, :] = row_hour_p

        return_days = return_days.append(df_model_day.iloc[1, :])

    return return_days
    '''
def adjust_df(dataframes_location):

    coordinates = pd.read_csv(dataframes_location, nrows=1)
    df = pd.read_csv(dataframes_location, skiprows=2)
    df.insert(0, 'Longitude', coordinates['Longitude'][0])
    df.insert(1, 'Latitude', coordinates['Latitude'][0])
    df = df.drop('Minute', axis=1)

    return df

data_loc = 'C:/Users/seforeros/OneDrive/Escritorio/proyectos/renewable/pruebas/csv_clara/1998/'

filtered_df = adjust_df(data_loc + '1224740_5.05_-74.62_1998.csv')

df_month = filtered_df.loc[filtered_df['Month'] == 1, :]


hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
data_day = {'Longitude':[],'Latitude':[],'Year': [],'Month': [],'Day': [],'DHI':[], 'DNI':[],'Wind Speed':[],
              'Temperature':[],'Pressure':[],'GHI':[],'Wind Direction':[]
}

month = calculate_day(df_month, hours, data_day)

print(df_month.columns)

