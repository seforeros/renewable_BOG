import cdsapi
'''
c = cdsapi.Client()

c.retrieve(
    'satellite-surface-radiation-budget',
    {
        'format': 'zip',
        'product_family': 'clara',
        'origin': 'eumetsat',
        'variable': [
            'surface_downwelling_longwave_flux', 'surface_downwelling_shortwave_flux', 'surface_upwelling_longwave_flux',
        ],
        'climate_data_record_type': 'thematic_climate_data_record',
        'time_aggregation': 'monthly_mean',
        'year': [
            '1990', '1991', '1992',
            '1993', '1994', '1995',
            '1996', '1997', '1998',
            '1999', '2000', '2001',
            '2002', '2003', '2004',
            '2005', '2006', '2007',
            '2008', '2009', '2010',
            '2011', '2012', '2013',
            '2014', '2015', '2016',
            '2017', '2018',
        ],
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'version': 'v2_0',
        'sensor_on_satellite': 'avhrr_on_multiple_satellites',
    },
    'download_clara.zip')

c2 = cdsapi.Client()

c2.retrieve(
    'satellite-surface-radiation-budget',
    {
        'format': 'zip',
        'product_family': 'clara',
        'origin': 'c3s',
        'variable': 'surface_upwelling_shortwave_flux',
        'climate_data_record_type': 'thematic_climate_data_record',
        'sensor_on_satellite': 'avhrr_on_multiple_satellites',
        'time_aggregation': 'monthly_mean',
        'year': [
            '1990', '1991', '1992',
            '1993', '1994', '1995',
            '1996', '1997', '1998',
            '1999', '2000', '2001',
            '2002', '2003', '2004',
            '2005', '2006', '2007',
            '2008', '2009', '2010',
            '2011', '2012', '2013',
            '2014', '2015', '2016',
            '2017', '2018',
        ],
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'version': 'v2_0_1',
    },
    'download_clara2.zip')
'''
c3 = cdsapi.Client()
c3.retrieve(
    'satellite-surface-radiation-budget',
    {
        'format': 'zip',
        'product_family': 'cci',
        'origin': 'esa',
        'variable': 'all_variables',
        'climate_data_record_type': 'thematic_climate_data_record',
        'sensor_on_satellite': [
            'aatsr_on_envisat', 'atsr2_on_ers2',
        ],
        'time_aggregation': 'monthly_mean',
        'year': [
            '1995', '1996', '1997',
            '1998', '1999', '2000',
            '2001', '2002', '2003',
            '2004', '2005', '2006',
            '2007', '2008', '2009',
            '2010', '2011', '2012',
        ],
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
    },
    'download_clara3.zip')