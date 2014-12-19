from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(name='cloudstats',
      version='0.1',
      description="""Library to calculate the cloud cover rate from Landsat 8
          scenes metadata.""",
      long_description=long_description,
      classifiers=[],
      keywords='landsat, clouds, stats, pandas',
      author="Wille Marcel",
      author_email='wille.marcel@hexgis.com',
      url='https://github.com/ibamacsr/cloudstats',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
          'pandas',
          'simplejson'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      cloudstats=cloudstats.scripts.cli:cli
      """
      )
