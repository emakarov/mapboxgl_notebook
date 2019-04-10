import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('README.md') as f:
    long_description = f.read()

setup(
    name='mapboxgl_notebook',
    version='0.7',
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
    long_description=long_description,
    long_description_content_type="text/markdown",
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
