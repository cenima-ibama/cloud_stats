cloudstats
==========

A Python library to calculate the cloud cover rate from Landsat 8 scenes metadata.

Installation
=======

    pip install git+https://github.com/ibamacsr/cloudstats.git/#egg=cloudstats

Usage
=======

    Usage: cloudstats [OPTIONS] <start_date> <end_date> <geojson_scene_list>
                      <landsat_file>

      Get cloud rate for a determined period and scene list.

    Options:
      --help  Show this message and exit.

Requirements
======
    * click
    * pandas
    * simplejson

License
======

GPLv3
