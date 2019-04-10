"""MapboxGL map layers."""
from mapboxgl_notebook.properties import Paint


class BaseLayer:
    """Base layer class."""

    #: GeoJSON geometry type of the layer
    geojson_geometry_type = ''
    #: Mapbox layer type
    mapbox_layer_type = ''

    def __init__(self, source, layer_id=None, layer_filter=None, paint=None, below_layer_id=None):
        """Initialisation of BaseLayer.

        :param source: GeoJSON for this layer.
        :type source: :class: `sources.GeoJSONSource`
        :param layer_id: mapbox layer ID. Default (if None) is defined in default_layer_id()
        :type layer_id: str
        :param layer_filter: Layer filter expression for mapbox
        :type layer_filter: dict
        :param below_layer_id: Layer should be below layer with ID below_layer_id
        :type below_layer_id: str
        """
        self.source = source
        self._layer_id = layer_id
        self._filter = layer_filter
        self._paint = paint
        self._below_layer_id = below_layer_id

    def default_layer_id(self):
        """Returns default layer ID."""
        return '{}_{}'.format(self.geojson_geometry_type, self.source.source_id)

    def layer_id(self):
        """Returns layer_id."""
        return self._layer_id or self.default_layer_id()

    def default_filter(self):
        """Returns default mapbox filter expression."""
        return ['==', ['geometry-type'], self.geojson_geometry_type]

    def filter(self):
        """Returns filter expression for mapbox."""
        return self._filter or self.default_filter()

    def default_paint(self):
        return Paint()

    def paint(self):
        """Returns paint expression."""
        paint = self._paint or self.default_paint()
        return paint.data

    def to_dict(self):
        """Returns dictionary with layer data."""
        return {
            'id': self.layer_id(),
            'source': self.source.source_id,
            'type': self.mapbox_layer_type,
            'paint': self.paint(),
            'filter': self.filter(),
            'below_layer_id': self._below_layer_id
        }


class PointCircleLayer(BaseLayer):
    """Layer of Point geojson geometry objects represented as mapbox circle layer."""

    #: GeoJSON geometry type of the layer: Point
    geojson_geometry_type = 'Point'
    #: Mapbox layer type: circle
    mapbox_layer_type = 'circle'

    def default_paint(self):
        """Returns paint expression."""
        paint = Paint(
            circle_radius=4,
            circle_color='#0000ff',
        )
        return paint


class LineStringLineLayer(BaseLayer):
    """Layer of LineStrings represented as line layer."""

    #: GeoJSON geometry type of the layer: LineString
    geojson_geometry_type = 'LineString'
    #: Mapbox layer type: circle
    mapbox_layer_type = 'line'

    def default_paint(self):
        """Returns paint expression."""
        paint = Paint(
            line_color='#0000ff',
        )
        return paint


class PolygonFillLayer(BaseLayer):

    #: GeoJSON geometry type of the layer: LineString
    geojson_geometry_type = 'Polygon'
    #: Mapbox layer type: circle
    mapbox_layer_type = 'fill'

    def default_paint(self):
        """Returns paint expression."""
        paint = Paint(
            fill_color='#0000ff',
        )
        return paint
