from typing import List
from matrix.algorithm import get_matrix
from matrix.services import get_elements
import pytest
import asyncio


@pytest.fixture
def matrix_url():
    return 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'


@pytest.fixture
def get_traversal():
    return [
        10, 50, 90, 130,
        140, 150, 160, 120,
        80, 40, 30, 20,
        60, 100, 110, 70,
    ]


def test_get_elements():
    result: List[int] = get_elements('|  10 |  20 |  30 |  40 |')
    assert result == ['10', '20', '30', '40'], result


def test_get_matrix(matrix_url, get_traversal):
    assert asyncio.run(get_matrix(matrix_url)) == get_traversal
