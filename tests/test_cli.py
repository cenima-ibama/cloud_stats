from click.testing import CliRunner

from cloudstats.scripts.cli import cli


def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli,
        ['20141201', '20141216', 'tests/test.geojson', 'tests/lc8_test.csv']
        )
    assert result.exit_code == 0
    assert result.output == "20141201 - 20141216 - Rate of clouds: 7.76\n"
