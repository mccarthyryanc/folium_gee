#! /usr/bin/env python
#
#
import ee
import folium

ee.Initialize()

def folium_gee_map(image,vis_params=None,folium_kwargs={}):
    """
    Function to view Google Earch Engine tile layer as a Folium map.
    
    Parameters
    ----------
    image : Google Earth Engine Image.
    vis_params : Dict with visualization parameters.
    folium_kwargs : Keyword args for Folium Map.
    """
    
    # Get the MapID and Token after applying parameters
    image_info = image.getMapId(vis_params)
    mapid = image_info['mapid']
    token = image_info['token']
    folium_kwargs['attr'] = ('Map Data &copy; <a href="https://earthengine.google.com/">Google Earth Engine</a> ')
    folium_kwargs['tiles'] = "https://earthengine.googleapis.com/map/%s/{z}/{x}/{y}?token=%s"%(mapid,token)
    
    return folium.Map(**folium_kwargs)

def folium_gee_layer(folium_map,image,vis_params=None,folium_kwargs={}):
    """
    Function to add Google Earch Engine tile layer as a Folium layer.
    
    Parameters
    ----------
    folium_map : Folium map to add tile to.
    image : Google Earth Engine Image.
    vis_params : Dict with visualization parameters.
    folium_kwargs : Keyword args for Folium Map.
    """
    
    # Get the MapID and Token after applying parameters
    image_info = image.getMapId(vis_params)
    mapid = image_info['mapid']
    token = image_info['token']
    folium_kwargs['attr'] = ('Map Data &copy; <a href="https://earthengine.google.com/">Google Earth Engine</a> ')
    folium_kwargs['tiles'] = "https://earthengine.googleapis.com/map/%s/{z}/{x}/{y}?token=%s"%(mapid,token)
    
    layer = folium.TileLayer(**folium_kwargs)
    layer.add_to(folium_map)

def test_add_layer(html=None):
    """
    Test adding layers
    """

    lat = 37
    lon = -118
    zoom_start=4

    # Open Street Map Base
    m = folium.Map(location=[lat, lon], tiles="OpenStreetMap", zoom_start=zoom_start)

    # Add GEE Terrain Layer
    image = ee.Image('srtm90_v4')
    vis_params = {'min':0.0, 'max':3000, 'palette':'00FFFF,0000FF'}
    folium_gee_layer(m,image,vis_params=vis_params,folium_kwargs={'overlay':True,'name':'SRTM'})

    # Create a reference to the image collection
    l8 = ee.ImageCollection('LANDSAT/LC8_L1T_TOA')
    # Filter the collection down to a two week period
    filtered = l8.filterDate('2013-05-01', '2013-05-15');
    # Use the mosaic reducer, to select the most recent pixel in areas of overlap
    l8_image = filtered.median()
    l8_vis_params = {'min': 0, 'max':0.3}
    folium_gee_layer(m,l8_image,l8_vis_params,folium_kwargs={'overlay':True,'name':'Visual'})
    m.add_child(folium.LayerControl())
    
    if html is None:
        html = 'index.html'
    
    print("Saving map as: {0}".format(html))
    m.save(html)

def test_add_map(html=None):
    """
    Test add map baselayer
    """

    lat = 37
    lon = -118
    zoom_start=4

    # Add GEE Terrain as new Map
    image = ee.Image('srtm90_v4')
    vis_params = {'min':0.0, 'max':3000}
    folium_params={'location':[lat, lon],
                   'zoom_start':zoom_start}
    m = folium_gee_map(image,vis_params=vis_params,folium_kwargs=folium_params)

    # Create a reference to the image collection
    l8 = ee.ImageCollection('LANDSAT/LC8_L1T_TOA')
    # Filter the collection down to a two week period
    filtered = l8.filterDate('2013-05-01', '2013-05-15');
    # Use the mosaic reducer, to select the most recent pixel in areas of overlap
    l8_image = filtered.median()
    l8_vis_params = {'min': 0, 'max':0.3}
    folium_params = {'overlay':True,'name':'Visual'}
    folium_gee_layer(m,l8_image,l8_vis_params,folium_kwargs=folium_params)
    m.add_child(folium.LayerControl())

    if html is None:
        html = 'index.html'

    print("Saving map as: {0}".format(html))
    m.save(html)

if __name__ == '__main__':
    test_add_map('gee_map_test.html')
    test_add_layer('gee_layer_test.html')