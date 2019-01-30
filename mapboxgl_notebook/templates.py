from jinja2 import Environment, PackageLoader, StrictUndefined

env = Environment(
    loader=PackageLoader('mapboxgl_notebook', 'templates'),
    autoescape=False,
    undefined=StrictUndefined
)


def format(template, **kwargs):
    template = env.get_template(template)
    return template.render(**kwargs)
