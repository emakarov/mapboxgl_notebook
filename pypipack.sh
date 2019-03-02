#!/bin/bash
echo "removing build dist mapboxgl_notebook.egg-info ..."
rm -r build
rm -r dist
rm -r mapboxgl_notebook.egg-info
echo "generating dist..."
python setup.py sdist bdist_wheel
echo "twine uploading to pypi..."
twine upload dist/*
