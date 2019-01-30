# mapboxgl_notebook

MapboxGL for ipython notebook with multilayer support and flexibility.

Initially I worked with ipython notebook library provided by mapbox, but it had some disadvantages:
1. Does not support multi-layer.
2. A lot of templates and complicated logic.
3. Limited ability to use mapboxgl expressions (especially, new-style expressions).

I have implemented pull request to that repository to support multi-layer, as well as some other,
but due to lack of PR ownershipt this functionality was not supported in mapboxgl_jupyter at 31Jan2019

So, this project was created with taking into account:
1. Multi layer support from the very beginning.
2. Small amount of python, html and javascript code.
3. Support of mapboxgl expressions.
4. High flexibility to create new types of layers.

Examples:
```
import os
from mapboxgl_notebook.map import MapboxMap
from mapboxgl_notebook.sources import GeoJSONSource
from mapboxgl_notebook.layers import PointCircleLayer, LineStringLineLayer, PolygonFillLayer
from mapboxgl_notebook.properties import Paint
from mapboxgl_notebook.interactions import ClickInteraction, HoverInteraction
access_token = os.environ.get('MAPBOX_ACCESS_TOKEN')

# Data from dictionary
data = {
    'type': 'FeatureCollection',
    'features':  [
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [103.8198, 1.3521]
            },
            'properties': {
                'id': 1,
                'name': 'My first point'
            }
        },
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [103.8290, 1.3531]
            },
            'properties': {
                'id': 2,
                'name': 'My second point'
            }
        }
    ]
}
# Definition of source
source = GeoJSONSource(data, source_id='points')
# Layer (geojson type Point, mapboxgl type Circle)
layer = PointCircleLayer(source)
# Hover interaction (popup with property name)
hover = HoverInteraction(layer, properties=['name'])
# Map rendering
mapbox_map = MapboxMap(
    access_token=access_token,
    sources=[source],  # can be list of sources
    layers=[layer],  # can be list of layers
    interactions=[hover]
)
mapbox_map.show()

# Same as above but with Click interaction instead of hover
layer = PointCircleLayer(source)
click = ClickInteraction(layer, properties=['name'])
mapbox_map = MapboxMap(
    access_token=access_token,
    sources=[source],
    layers=[layer],
    interactions=[click]
)
mapbox_map.show()

# Data-driven properties directly with mapbox gl expressions
data_url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson'
source = GeoJSONSource(data_url, source_id='earthquakes')
paint = Paint(
    circle_color=[
            'interpolate', ["linear"], 
            ['get', 'mag'],
            1.3, '#0000ff',
            2, '#ff0000'
    ]
)
layer = PointCircleLayer(source, paint=paint)
interaction = ClickInteraction(layer, properties=['place', 'mag', 'type'])
mapbox_map = MapboxMap(
    center=[0,0],
    zoom=1,
    access_token=access_token,
    sources=[source],
    layers=[layer],
    interactions=[interaction]
)
mapbox_map.show()

# Polygon layer
data_url = 'https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_1_states_provinces_shp.geojson'
source = GeoJSONSource(data_url, source_id='states')
paint = Paint(
    fill_color='rgba(200, 100, 240, 0.4)',
    fill_outline_color='rgba(200, 100, 240, 1)'
)
layer = PolygonFillLayer(source, paint=paint)
interaction = ClickInteraction(layer)
mapbox_map = MapboxMap(
    center=[0,0],
    zoom=1,
    access_token=access_token,
    sources=[source],
    layers=[layer],
    interactions=[interaction]
)
mapbox_map.show()

```
