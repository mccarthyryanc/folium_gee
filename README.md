# FoliumGEE

A few simple functions to render Google Earth Engine Tile Layers with Folium.

Take a look at the tests directory for usage, but here is a simple example:

```python
import ee
import folium
import foliumgee

ee.Initialize()

image = ee.Image('srtm90_v4')
m = foliumgee.map(image)
m.save('srtm.html')
```