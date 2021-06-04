# Django Model Mixin Example

This is a simple example of using mixins with Django models. This is more of simple how-to, not an actual, full fledged demo. You are more than welcome to fork this repository and build out more logic yourself!

Directories

- config - Contians Django project files (settings.py, wsgi.py, etc)
- core - Contains all core logic that our other apps can use. Check models.py to see small, contianed models that we can use to create any number of mixins. In mixins.py, you will an example of creating a mixin with a few base models.
- account - A normal, Django app. In the models.py file, you will find an example of a model that inherits a base model and uses a mixin.

You can find the article for this repository on my blog at 

or on Medium at