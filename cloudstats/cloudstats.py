import simplejson
from subprocess import call
from datetime import datetime
from pandas import read_csv


def get_scene_names(geojson_file):
    """Open a geojson file and get the scene names list."""
    json = open(geojson_file, 'r').read()
    data = simplejson.loads(json)
    return [scene['properties']['name'] for scene in data['features']]


def get_metadata():
    """Download Landsat 8 metadata file."""
    call(['wget', 'http://landsat.usgs.gov/metadata_service/bulk_metadata_files/LANDSAT_8.csv'])


class Stats(object):

    def __init__(self, start_date, end_date, scene_list, landsat='LANDSAT_8.csv'):
        self.start_date = datetime.strptime(start_date, '%Y%m%d').date()
        self.end_date = datetime.strptime(end_date, '%Y%m%d').date()
        self.scene_list = scene_list
        self.data = read_csv(
            landsat,
            parse_dates=['acquisitionDate'],
            usecols=['path', 'row', 'acquisitionDate', 'cloudCoverFull']
            )

    def filter_by_date(self):
        """Filter the Landsat scenes by date of acquisition."""
        filtered_data = self.data[(
            (self.data['acquisitionDate'] >= self.start_date) &
            (self.data['acquisitionDate'] <= self.end_date)
            )]

        return filtered_data

    def filter_by_scenes(self, data=None):
        """Filter the Landsat scenes by path and row, using the scene_list
        parameter."""
        if data is None:
            data = self.data

        data_list = data.values.tolist()
        selected = []

        for item in data_list:
            path_row = '%s-%s' % (item[1], item[2])
            if path_row in self.scene_list:
                selected.append(item)

        return selected

    def calc_rate(self, data=None):
        """Calculate the cloud cover rate of Landsat scenes."""
        if data is None:
            data = self.data

        if type(data) != list:
            data = data.values.tolist()

        clouds = [i[-1] for i in data]

        if len(clouds) == 0:
            return "No scenes selected"
        else:
            return sum(clouds) / len(clouds)

    def full_calc(self):
        """Calculate the cloud cover rate from filtered scenes."""
        return self.calc_rate(self.filter_by_scenes(self.filter_by_date()))