def Satellite(parameters, region, map_data):
    import ee
    
    #Delimitacion de Bogota
    bogota_urbano = ee.FeatureCollection('projects/ee-seforeros/assets/2022_perimetro_urbano')
    bogota_protegidas = ee.FeatureCollection('projects/ee-seforeros/assets/2022_areas_protegidas_sinap')
    bogota_rural = ee.FeatureCollection('projects/ee-seforeros/assets/2022_territorio_rural')
    
    #Variables a considerar
    source = parameters.get('source')
    variable = parameters.get('variable')
    band = parameters.get('band')
    units = parameters.get('units')
    max_value = parameters.get('max_value')
    min_value = parameters.get('min_value')
    start = parameters.get('start')
    end = parameters.get('end')

    #Descarga de datos
    image_region = ee.ImageCollection(source).filterBounds(region)
    image_time = image_region.select(band).filterDate(start, end)
    image_final = image_time.map(lambda image: image.clip(region))

    #Banda de datos
    band_viz = {
      'min': min_value,
      'max': max_value,
      'palette': ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
    }
    map_data.setCenter(-74.2, 4.3, 9)
    map_data.addLayer(image_final, band_viz, variable, 1, 0.8)

    #Paleta de colores
    colors = band_viz['palette']
    vmin = band_viz['min']
    vmax = band_viz['max']

    map_data.add_colorbar(band_viz, label= variable + units)
    map_data.addLayerControl()

    #Capas de areas de interes
    map_data.addLayer (bogota_rural, {'color':"0000FF"} , "Territorio Rural",1)
    map_data.addLayer(bogota_protegidas,{'color':"FF0000"},'Áreas protegidas SINAP 2022',1)
    map_data.addLayer(bogota_urbano,{'color':"000000"},'Perímetro urbano 2022', 1)

    legend_dict_data = {
        'Territorio Rural': '0000FF',
        'Áreas protegidas SINAP 2022': 'FF0000',
        'Perímetro urbano 2022': '000000'
    }
    map_data.add_legend(legend_tittle = "Áreas de interés", legend_dict = legend_dict_data)

    
def Bogota_IDEAM(region, map_IDEAM):
    import ee
    
    bogota_urbano = ee.FeatureCollection('projects/ee-seforeros/assets/2022_perimetro_urbano')
    bogota_protegidas = ee.FeatureCollection('projects/ee-seforeros/assets/2022_areas_protegidas_sinap')
    bogota_rural = ee.FeatureCollection('projects/ee-seforeros/assets/2022_territorio_rural')
    estaciones = ee.FeatureCollection('projects/ee-seforeros/assets/CNE_IDEAM').filterBounds(region)
    
    map_IDEAM.setCenter(-74.2, 4.3, 9)

    map_IDEAM.addLayer (bogota_rural, {'color':"blue"} , "Territorio Rural",1,0.5)
    map_IDEAM.addLayer(bogota_urbano,{'color':"black"},'Perímetro urbano 2022', 1, 0.5)
    map_IDEAM.addLayer(bogota_protegidas,{'color':"red"},'Áreas protegidas SINAP 2022',1, 0.5)
    map_IDEAM.addLayer(estaciones,{'color':"green"},'CNE IDEAM',1)

    legend_dict = {
        'Territorio Rural': '0000FF',
        'Perímetro urbano 2022': '000000',
        'Áreas protegidas SINAP 2022': 'FF0000',
        'CNE IDEAM': '00FF00'
    }

    map_IDEAM.add_legend(legend_tittle = "Áreas de interés", legend_dict = legend_dict)
    
def Image(parameters, region, map_data):
    import ee
    
    #Delimitacion de Bogota
    bogota_urbano = ee.FeatureCollection('projects/ee-seforeros/assets/2022_perimetro_urbano')
    bogota_protegidas = ee.FeatureCollection('projects/ee-seforeros/assets/2022_areas_protegidas_sinap')
    bogota_rural = ee.FeatureCollection('projects/ee-seforeros/assets/2022_territorio_rural')
    
    #Variables a considerar
    source = parameters.get('source')
    variable = parameters.get('variable')
    units = parameters.get('units')
    max_value = parameters.get('max_value')
    min_value = parameters.get('min_value')
    start = parameters.get('start')
    end = parameters.get('end')
    
    #Descarga de datos
    image_region = ee.Image(source)
    image_final = image_region.clip(region)

    #Banda de datos
    band_viz = {
      'min': min_value,
      'max': max_value,
      'palette': ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']
    }
    map_data.setCenter(-74.2, 4.3, 9)
    map_data.addLayer(image_final, band_viz, variable, 1)

    #Paleta de colores
    colors = band_viz['palette']
    vmin = band_viz['min']
    vmax = band_viz['max']

    map_data.add_colorbar(band_viz, label= variable + units)
    map_data.addLayerControl()

    #Capas de areas de interes
    map_data.addLayer (bogota_rural, {'color':"0000FF"} , "Territorio Rural",1, 0.8)
    map_data.addLayer(bogota_protegidas,{'color':"FF0000"},'Áreas protegidas SINAP 2022',1, 0.8)
    map_data.addLayer(bogota_urbano,{'color':"000000"},'Perímetro urbano 2022', 1, 0.8)

    legend_dict_data = {
        'Territorio Rural': '0000FF',
        'Áreas protegidas SINAP 2022': 'FF0000',
        'Perímetro urbano 2022': '000000'
    }
    map_data.add_legend(legend_tittle = "Áreas de interés", legend_dict = legend_dict_data)