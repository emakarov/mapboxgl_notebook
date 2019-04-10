# mapboxgl_notebook

MapboxGL for ipython notebook with multilayer support and flexibility.

If you were looking for multilayer mapboxgl ipython module, this repository is a right place.

This project was created with taking into account:
1. Multi layer support from the very beginning.
2. Small amount of python, html and javascript code.
3. Support of mapboxgl expressions.
4. High flexibility to create new types of layers.

Installation:
download code, install with pip from github or from pypi:

```
pip install mapboxgl_notebook
```

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
```
![map with points and hover](https://user-images.githubusercontent.com/395963/52003949-e98bed00-2500-11e9-9fa5-ee0356667fcc.png)
```

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
```
![map with points and click](https://user-images.githubusercontent.com/395963/52003955-ec86dd80-2500-11e9-96d7-938fb5e2eee7.png)
```
# Data-driven properties directly with mapbox gl expressions (picture can be different - real world dataset!)
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
    style='mapbox://styles/mapbox/dark-v9',  # lets use another style
    center=[0,0],
    zoom=1,
    access_token=access_token,
    sources=[source],
    layers=[layer],
    interactions=[interaction]
)
mapbox_map.show()
```
![map with data driven color](https://user-images.githubusercontent.com/395963/52004296-bd24a080-2501-11e9-8921-fa36b1c79af5.png)
```

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
![map with polygons](https://user-images.githubusercontent.com/395963/52003958-ef81ce00-2500-11e9-80af-feb3eb526fdc.png)

```
# How to place one layer below another:
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
                'coordinates': [103.8798, 1.3831]
            },
            'properties': {
                'id': 1,
                'text_for_layer_1': 'Hello point 1 layer 1',
                'text_for_layer_2': 'Hello point 1 layer 2'
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
                'text_for_layer_1': 'Hello point 2 layer 2',
                'text_for_layer_2': 'Hello point 2 layer 2'
            }
        }
    ]
}
# Definition of source
source = GeoJSONSource(data, source_id='points')
# Layer (geojson type Point, mapboxgl type Circle)
layer = PointCircleLayer(source, layer_id='layer_points')
layer2 = PointCircleLayer(
    source,
    paint=Paint(circle_radius=10, circle_color='#00ff00'),
    below_layer_id='layer_points'
)
# Hover interaction (popup with property name)
hover = HoverInteraction(layer, properties=['text_for_layer_1'])
hover2 = HoverInteraction(layer2, properties=['text_for_layer_2'])
# Map rendering
mapbox_map = MapboxMap(
    access_token=access_token,
    sources=[source],  # can be list of sources
    layers=[layer, layer2],  # can be list of layers
    interactions=[hover, hover2]
)
mapbox_map.show()
```
