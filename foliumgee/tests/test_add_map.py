import os
import ee
import folium
import foliumgee

ee.Initialize()

def test_map(html=None):
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
    m = foliumgee.map(image,vis_params=vis_params,folium_kwargs=folium_params,
                      name='SRTM')

    # Create a reference to the image collection
    l8 = ee.ImageCollection('LANDSAT/LC8_L1T_TOA')
    # Filter the collection down to a two week period
    filtered = l8.filterDate('2013-05-01', '2013-05-15');
    # Use the mosaic reducer, select the most recent pixel in overlap areas
    l8_image = filtered.median()
    l8_vis_params = {'min': 0, 'max':0.3}
    folium_params = {'overlay':True,'name':'Visual'}
    foliumgee.layer(m,l8_image,l8_vis_params,folium_kwargs=folium_params)
    m.add_child(folium.LayerControl())

    if html is None:
        html = 'test_map.html'
    m.save(html)

    assert os.path.exists(html)
