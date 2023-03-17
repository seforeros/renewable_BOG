import pandas as pd

def ee_array_to_df(arr, list_of_bands):
    """Transforms client-side ee.Image.getRegion array to pandas.DataFrame.
    Modification of 
    https://developers.google.com/earth-engine/tutorials/community/intro-to-python-api-guiattard
    """
    df = pd.DataFrame(arr)

    # Rearrange the header.
    headers = df.iloc[0]
    df = pd.DataFrame(df.values[1:], columns=headers)

    # Remove rows without data inside.
    df = df[['longitude', 'latitude', 'time', *list_of_bands]]

    # Convert the data to numeric values.
    for band in list_of_bands:
        df[band] = pd.to_numeric(df[band], errors='coerce')

    # Convert the time field into a datetime.
    df['date'] = pd.to_datetime(df['time'], unit='ms')
    # Keep the columns of interest.
    df = df[['date', 'longitude', 'latitude', *list_of_bands]]

    return df

def collection_data(parameters, region, scale_value):
    import ee
    
    i_date = parameters.get('start')
    f_date = parameters.get('end')
    layer = parameters.get('band')
    source = parameters.get('source')
    
    bands = [layer]

    collection = ee.ImageCollection(source).filterDate(
            ee.Date(i_date), ee.Date(f_date)
        ).select(layer)

    # now perform the clipping and dataframe conversion 
    collection_area_of_interest = collection.getRegion(region, scale = scale_value).getInfo()
    
    #define the dataframe to export
    df_area_of_interest = ee_array_to_df(collection_area_of_interest, bands)
    
    return df_area_of_interest