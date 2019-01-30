"""Interactions with data."""


class Interaction:

    interaction_type = 'interaction'

    def __init__(self, layer, properties='*'):
        self.layer = layer
        self.properties = properties

    def to_dict(self):
        return {}


class HoverInteraction(Interaction):

    interaction_type = 'hover'

    def __init__(self, layer, properties='*'):
        super().__init__(layer, properties=properties)

    def to_dict(self):
        return {
            'layer_id': self.layer.layer_id(),
            'interaction_type': self.interaction_type,
            'properties': self.properties
        }


class ClickInteraction(HoverInteraction):

    interaction_type = 'click'
