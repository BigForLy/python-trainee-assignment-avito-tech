import asyncio
from matrix.requests import get_text_by_url
import pytest


@pytest.fixture
def matrix_url():
    return 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'


def test_requests_success(matrix_url):
    result: str = asyncio.run(get_text_by_url(matrix_url))
    assert result != "", result
