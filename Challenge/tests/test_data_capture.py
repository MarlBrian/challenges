import pytest
from DataCapture import DataCapture


@pytest.fixture
def DataCaptureObject():
    dc = DataCapture()
    list = [3,9,3,4,6]
    for ele in list:
        dc.add(ele)
    return dc


@pytest.fixture
def DataCaptureEmptyObject():
    dc = DataCapture()
    return dc


@pytest.fixture
def DataCaptureStatsObject():
    dc = DataCapture()
    list = [3, 9, 3, 4, 6]
    for ele in list:
        dc.add(ele)
    dc.build_stats()
    return dc


def test_datacapture_add(DataCaptureEmptyObject):
    DataCaptureEmptyObject.add(0)
    assert 1 == len(DataCaptureEmptyObject.queue)


def test_datacapture_add_missing_value(DataCaptureEmptyObject):
    with pytest.raises(TypeError):
        DataCaptureEmptyObject.add()


def test_datacapture_add_incorrect_type(DataCaptureEmptyObject):
    with pytest.raises(TypeError):
        DataCaptureEmptyObject.add('s')


def test_datacapture_buildstats(DataCaptureObject):
    DataCaptureObject.build_stats()
    assert 2 == DataCaptureObject.stats[3][1]


def test_datacapture_less(DataCaptureStatsObject):
    assert 2 == DataCaptureStatsObject.less(4)


def test_datacapture_less_missing_value(DataCaptureStatsObject):
    with pytest.raises(TypeError):
        DataCaptureStatsObject.less()


def test_datacapture_less_incorrect_type(DataCaptureStatsObject):
    with pytest.raises(TypeError):
        DataCaptureStatsObject.less('s')


def test_datacapture_between(DataCaptureStatsObject):
    assert 4 == DataCaptureStatsObject.between(3,6)


def test_datacapture_between_missing_args(DataCaptureStatsObject):
    with pytest.raises(TypeError):
        DataCaptureStatsObject.between()


def test_datacapture_between_incorrect_type(DataCaptureStatsObject):
    with pytest.raises(TypeError):
        DataCaptureStatsObject.between(3,'s')


def test_datacapture_greater(DataCaptureStatsObject):
    assert 2 == DataCaptureStatsObject.greater(4)


def test_datacapture_greater_missing_value(DataCaptureStatsObject):
    with pytest.raises(TypeError):
        DataCaptureStatsObject.greater()


def test_datacapture_greater_incorrect_type(DataCaptureStatsObject):
    with pytest.raises(TypeError):
        DataCaptureStatsObject.greater('s')
