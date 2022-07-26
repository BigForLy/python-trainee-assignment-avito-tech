import asyncio
from typing import List
from requests import get_text_by_url
import httpx
from main import get_matrix, get_elements

url = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'


def test_requests_success():
    result: httpx.Response = asyncio.run(get_text_by_url(url))
    assert result.status_code == 200, result.text


def test_get_elements():
    result: List[int] = get_elements('|  10 |  20 |  30 |  40 |')
    assert result == ['10', '20', '30', '40'], result


def test_get_matrix():
    TRAVERSAL = [
        10, 50, 90, 130,
        140, 150, 160, 120,
        80, 40, 30, 20,
        60, 100, 110, 70,
    ]
    assert asyncio.run(get_matrix(url)) == TRAVERSAL
