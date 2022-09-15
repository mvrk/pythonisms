from pythonic import __version__
from pythonic.pythonic import *
import pytest


def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture
def data():
    lists = LinkedList()
    lists.insert(2)
    lists.insert(3)
    lists.insert(5)

    return lists


def test_len_of_list(data):
    assert len(data) == 3


def test_dunder_str_method(data):
    assert str(data) == "[5] -> [3] -> [2] -> None"


def test_dunder_get_item_method(data):
    assert data[1] == 3


def test_dunder_itrate(data):
    expected = [5, 3, 2]
    for idx, item in enumerate(data):
        assert item == expected[idx]
