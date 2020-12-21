# TODO: Fill out this file with information about your package

# HINT: Go back to the object-oriented programming lesson "Putting Code on PyPi" and "Exercise: Upload to PyPi"

# HINT: Here is an example of a setup.py file
# https://packaging.python.org/tutorials/packaging-projects/
import setuptools

setuptools.setup(
                name='package_dsnd_pmherp',
                version='0.0.1',
                author='pmherp',
                author_email='pmherp.git@gmail.com',
                description='package on OOP for barplots',
                packages=['package_dsnd_pmherp'],
                zip_safe=False
                )