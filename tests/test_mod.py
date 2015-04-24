from cloudstats.cloudstats import Stats


def test_filter_by_date():
    test_1 = Stats('20141201', '20141216', ['156-65'], 'tests/lc8_test.csv')
    test_2 = Stats('20141217', '20141231', ['156-65'], 'tests/lc8_test.csv')
    assert len(test_1.filter_by_date()) == 3
    assert len(test_2.filter_by_date()) == 0


def test_filter_by_scenes():
    test_1 = Stats('20141201', '20141216', ['156-65','156-66'], 'tests/lc8_test.csv')
    test_2 = Stats('20141201', '20141216', ['156-225'], 'tests/lc8_test.csv')
    assert len(test_1.filter_by_scenes()) == 2
    assert len(test_2.filter_by_scenes()) == 1


def test_calc_rate():
    test_1 = Stats('20141201', '20141216', ['156-65','156-66'], 'tests/lc8_test.csv')
    assert test_1.calc_rate() == (0 + 3.04 + 12.48) / 3
    assert test_1.full_calc() == (3.04 + 12.48) / 2
