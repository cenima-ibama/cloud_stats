# Skeleton of a CLI

import click

import cloudstats


@click.command('cloudstats')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(cloudstats.has_legs)
