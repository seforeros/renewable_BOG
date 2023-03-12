import cdsapi

c = cdsapi.Client()

c.retrieve(
    'satellite-earth-radiation-budget',
    {
        'format': 'zip',
        'origin': 'nasa_ceres_ebaf',
        'variable': 'outgoing_longwave_radiation',
        'year': '2003',
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'area': [
            5, -74, 3,
            73,
        ],
    },
    'download.zip')

c.retrieve(
    'satellite-earth-radiation-budget',
    {
        'format': 'zip',
        'origin': 'esa_cloud_cci',
        'variable': 'all_available_variables',
        'sensor': [
            'aatsr', 'atsr2',
        ],
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
        'area': [
            5, -74, 3,
            -73,
        ],
    },
    'download2.zip')