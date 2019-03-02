import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='mapboxgl_notebook',
    version='0.2',
    packages=[
        'mapboxgl_notebook',
    ],
    package_data={
        'mapboxgl_notebook': ['templates/*']
    },
    install_requires=[
        'mapboxgl',
        'IPython',
        'jinja2',
        'nssjson',
    ],
    extras_require={},
    include_package_data=True,
    license='BSD License',  # example license
    description='MapboxGL ipython renderer',
    long_description='''
    MapboxGL for ipython notebook with multilayer support and flexibility.
    1. Multi layer support from the very beginning.
    2. Small amount of python, html and javascript code.
    3. Support of mapboxgl expressions.
    4. High flexibility to create new types of layers.

    See more information on https://github.com/emakarov/mapboxgl_notebook
    ''',
    url='https://github.com/emakarov/mapboxgl_notebook',
    zip_safe=False,
    author='Evgeni Makarov',
    author_email='evgeni.makarov@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Scientific/Engineering :: GIS',
    ],
)
