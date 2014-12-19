# Skeleton of a CLI

import click

from cloudstats.cloudstats import Stats, get_scene_names


@click.command('cloudstats')
@click.argument('start_date', type=str, metavar='<start_date>')
@click.argument('end_date', type=str, metavar='<end_date>')
@click.argument('geojson_scene_list', type=str, metavar='<geojson_scene_list>')
@click.argument('landsat_file', type=str, metavar='<landsat_file>')
def cli(start_date, end_date, geojson_scene_list, landsat_file):
    """Get cloud rate for a determined period and scene list."""
    scene_list = get_scene_names(geojson_scene_list)
    stats = Stats(start_date, end_date, scene_list, landsat_file)
    result = stats.full_calc()
    click.echo(
        "%s - %s - Rate of clouds: %s" % (start_date, end_date, result)
        )
