# mapboxgl_notebook

MapboxGL for ipython notebook with multilayer support and flexibility.

Initially I worked with ipython notebook library provided by mapbox, but it had some disadvantages:
1. Does not support multi-layer.
2. A lot of templates and complicated logic.
3. Limited ability to use mapboxgl expressions (especially, new-style expressions).

I have implemented pull request to that repository to support multi-layer, as well as some other,
but due to lack of PR ownershipt this functionality was not supported in mapboxgl_jupyter at 31Jan2019

So, this project was created with taking into account:
1. Multi layer support from the very beginning.
2. Small amount of python, html and javascript code.
3. Support of mapboxgl expressions.
4. High flexibility to create new types of layers.
