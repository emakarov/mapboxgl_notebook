"""MapboxGL map data sources."""
import nssjson


class GeoJSONSource:

    def __init__(self, data, source_id=None):
        self.data = data
        self.source_id = source_id
        self.type = 'geojson'

    def to_dict(self):
        """To JSON conversion."""
        return {
            'id': self.source_id,
            'data': self.data,
            'type': self.type,
        }
