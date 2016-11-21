from setuptools import setup, find_packages
import sys, os

version = '1'

setup(name='webemcrawler',
      version=version,
      description="Harvests email's and URL's",
      long_description="""\
Extract URL's and email's and stores them in a database.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Webscraper Webcrawler',
      author='Seth Fox',
      author_email='seth@technometro.com',
      url='http://technometro.com',
      license='Creative Commons BY-SA',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
