# FoliumGEE

A few simple functions to render Google Earth Engine Tile Layers with Folium.

Take a look at the tests directory for usage, but here is a simple example:

```python
import ee
import foliumgee

ee.Initialize()

image = ee.Image('srtm90_v4')
m = foliumgee.map(image)
m.save('srtm.html')
```

## Credentials

It is up to the user to either supply GEE credentials during the Initialization step:

```python
import ee

creds = ee.ServiceAccountCredentials(
	service_account,
	'privatekey.json')
ee.Initialize(creds)
```

or through via a [credentials file](https://developers.google.com/earth-engine/python_install_manual#setting-up-authentication-credentials).

## Install

Clone and install manually, or use pip:

```bash
# Method 1
git clone https://github.com/mccarthyryanc/folium_gee.git
cd folium_gee
python setup.py install
# Method 2
pip install git+https://github.com/mccarthyryanc/folium_gee.git
```
