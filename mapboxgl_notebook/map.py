"""
MapboxGL map.
Example:

.. code-block:: python

    from mapboxgl_notebook.map import MapboxMap
    from mapboxgl_notebook.sources import GeoJSONSource
    from mapboxgl_notebook.layers import PointCircleLayer, LineStringLineLayer
    from mapboxgl_notebook.properties import Paint
    from mapboxgl_notebook.interactions import HoverInteraction

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

    source = GeoJSONSource(data, source_id='points')
    layer = PointCircleLayer(source)
    hover = HoverInteraction(layer, properties=['name'])
    mapbox_map = MapboxMap(
        access_token=access_token,
        sources=[source],
        layers=[layer],
        interactions=[hover]
    )
    mapbox_map.show()

"""
import codecs
import os

import nssjson
from IPython.core.display import HTML, display

from mapboxgl_notebook import templates


class MapboxMap:

    def __init__(
            self,
            access_token=None,
            div_id='map',
            height='500px',
            width='100%',
            style='mapbox://styles/mapbox/streets-v9',
            center=[103.8198, 1.3521],
            zoom=10,
            sources=[],
            layers=[],
            styles=[],
            interactions=[]):
        """
        Initialisation of map.

        :param access_token: mapbox gel access token. will be taken from MAPBOX_ACCESS_TOKEN if None.
        :type access_token: str
        :param div_id: name of div_id (`map` by default)
        :type div_id: str
        :param height: css height of the map (default is `500px`)
        :type height: str
        :param width: css width of the map (default is `100%`)
        :type width: str
        :param style: mapboxgl base style (default is `'mapbox://styles/mapbox/streets-v9'`)
        :type style: str
        :param center: center position in [lon, lat] (default is [103.8198, 1.3521] - Singapore)
        :type center: list[float, float]
        :param zoom: starting map zoom (default is 10)
        :type zoom: float
        :param sources: list of sources for the map
        :type sources: list[:class: `mapboxgl_notebook.source.GeoJSONSource`]
        :param layers: list of layers for the map
        :type layers: list[one of :class: `mapboxgl_notebook.layers`]
        :param styles: list of styles for the map (not implemented yet)
        :type styles: list[one of :class: `mapboxgl_notebook.styles`]
        :param interactions: list of interactions for the map layers.
        :type interactions: list[one of :class: `mapboxgl_notebook.interactions`]
        """
        self.access_token = access_token or os.environ.get('MAPBOX_ACCESS_TOKEN', '')
        self.div_id = div_id
        self.height = height
        self.template = 'map.html'
        self.width = width
        self.style = style
        self.center = center
        self.zoom = zoom
        self.sources = sources
        self.layers = layers
        self.styles = styles
        self.interactions = interactions

    def as_iframe(self, html_data):
        """Build the HTML representation for the mapviz."""
        srcdoc = html_data.replace('"', "'")
        return (
            '<iframe id="{div_id}", srcdoc="{srcdoc}" style="width: {width}; '
                'height: {height};"></iframe>'.format(
                    div_id=self.div_id,
                    srcdoc=srcdoc,
                    width=self.width,
                    height=self.height
            )
        )

    def show(self, **kwargs):
        html = self.as_iframe(self.create_html(**kwargs))
        display(HTML(html))

    def create_html(self, filename=None):

        options = {
            'access_token': self.access_token,
            'div_id': self.div_id,
            'style': self.style,
            'center': self.center,
            'zoom': self.zoom,
            'sources': nssjson.dumps([source.to_dict() for source in self.sources], utc_datetime=True, iso_datetime=True),
            'layers': nssjson.dumps([layer.to_dict() for layer in self.layers], utc_datetime=True, iso_datetime=True),
            'styles': self.styles,
            'interactions': nssjson.dumps([interaction.to_dict() for interaction in self.interactions])
        }

        if filename:
            html = templates.format(self.template, **options)
            with codecs.open(filename, "w", "utf-8-sig") as f:
                f.write(html)
            return None
        else:
            return templates.format(self.template, **options)
