"""
Quick and dirty package to view Google Earh Engine Tile Layers in Folium Maps
"""
import folium

__version__ = 0.1

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

_gee_attr = ('Map Data &copy; <a href="https://earthengine.google.com/">'
             'Google Earth Engine</a> ')
_gee_url = "https://earthengine.googleapis.com/map/%s/{z}/{x}/{y}?token=%s"

def map(image,vis_params=None,folium_kwargs={}):
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
    folium_kwargs['attr'] = (_gee_attr)
    folium_kwargs['tiles'] = _gee_url%(mapid,token)
    
    return folium.Map(**folium_kwargs)

def layer(folium_map,image,vis_params=None,folium_kwargs={}):
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
    folium_kwargs['attr'] = (_gee_attr)
    folium_kwargs['tiles'] = _gee_url%(mapid,token)
    
    layer = folium.TileLayer(**folium_kwargs)
    layer.add_to(folium_map)