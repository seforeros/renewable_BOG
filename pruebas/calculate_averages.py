import numpy as np
import pandas as pd
import os

#funciones importantes

def adjust_df(dataframes_location):

    coordinates = pd.read_csv(dataframes_location, nrows=1)
    df = pd.read_csv(dataframes_location, skiprows=2)
    df.insert(0, 'Longitude', coordinates['Longitude'][0])
    df.insert(1, 'Latitude', coordinates['Latitude'][0])
    df = df.drop('Minute', axis=1)

    return df

def calculate_month(dataframe_filtered, months, hours, df_day, df_month):

    df_model_month = pd.DataFrame(df_month)

    for month in months:
        filtered_month = dataframe_filtered.loc[dataframe_filtered['Month'] == month, :]

        df_model_month_i = calculate_day(filtered_month, hours, df_day)
        #df_model_month_i = df_model_month_i.drop('Day', axis=1)

        #df_model_month_i[:,5:12] = df_model_month_i[:,5:12].mean()
        #month_i = df_model_month_i.describe()   #otros datos relevantes
        #month_i = month_i.drop('Day', axis=1)

        df_model_month = df_model_month.append(df_model_month_i)

    return df_model_month

def calculate_day(dataframe_month, hours, df_day):

    df_model_day = pd.DataFrame(df_day)
    return_days = pd.DataFrame(df_day)

    days = np.arange(1, dataframe_month['Day'].max()+1)

    for day in days:

        filtered_day = dataframe_month.loc[dataframe_month['Day'] == day, :]

        for hour in hours:
            if hour == 0:
                row_hour = filtered_day.loc[filtered_day['Hour'] == hour]

                df_model_day = df_model_day.append(row_hour)  #iteracion anterior
                df_model_day = df_model_day.append(row_hour)  #acumulado

            elif hour == 1:
                row_hour_p = filtered_day.loc[filtered_day['Hour'] == hour]

                df_model_day.iloc[1, :] = (df_model_day.iloc[0, :] + row_hour_p.iloc[0, :])/2
                df_model_day.iloc[0,:] = row_hour_p

            else:
                row_hour_p = filtered_day.loc[filtered_day['Hour'] == hour]

                df_model_day.iloc[1, :] = df_model_day.iloc[1, :] + (df_model_day.iloc[0, :] + row_hour_p.iloc[0, :])/2
                df_model_day.iloc[0, :] = row_hour_p

        trapecios = pd.DataFrame(df_model_day.iloc[1, [6, 7, 11]]).transpose()

        promedio_dia = pd.DataFrame(filtered_day.mean()).transpose()
        promedios = pd.DataFrame(promedio_dia.iloc[0, [0, 1, 2, 3, 4, 5, 8, 9, 12]]).transpose()

        return_days = pd.concat([promedios, trapecios], axis=1)

    return return_days

# codigo

years = ['1998', '1999']#, '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009']#,
#         '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

data_month = {'Longitude':[],'Latitude':[],'Year': [],'Month': [],'DHI':[], 'DNI':[],'Wind Speed':[],
              'Temperature':[],'Pressure':[],'GHI':[],'Wind Direction':[]
}

data_day = {'Longitude':[],'Latitude':[],'Year': [],'Month': [],'Day': [],'DHI':[], 'DNI':[],'Wind Speed':[],
              'Temperature':[],'Pressure':[],'GHI':[],'Wind Direction':[]
}

working_directory = 'C:/Users/seforeros/OneDrive/Escritorio/proyectos/renewable/pruebas/' #cambiar
years_folder = working_directory + 'csv_clara/' #cambiar
filtered_folder = working_directory + 'csv_filtered/'   #cambiar

for year in years:

    for filename in os.listdir(years_folder + year):

        filtered_df = adjust_df( years_folder + year + '/' + filename )

        df_year = calculate_month(filtered_df, months, hours, data_day, data_month)


        df_year.to_csv( filtered_folder + year + '/' + year + '.csv' )
'''
        df_month = filtered_df.loc[filtered_df['Month'] == 1, :]

        print(df_month.columns)
        print(np.arange(1, df_month['Day'].max() + 1))
        month = calculate_day(df_month, hours, data_day)
'''


        #print(filename + ' has been adjusted')

