from jinja2 import Environment, PackageLoader, StrictUndefined


env = Environment(
    loader=PackageLoader('mapboxgl_notebook', 'templates'),
    autoescape=False,
    undefined=StrictUndefined,
    extensions=['jinja2.ext.autoescape']
)


def format(template, **kwargs):
    template = env.get_template(template)
    return template.render(**kwargs)
