from typing import List
from collections import deque
import httpx
from .direction import DownDirection
from .services import get_elements
from .consts import CODE_OK
from .requests import get_text_by_url


class Algorithm:
    def __init__(self) -> None:
        self.xs: List[deque[str]] = []
        self.direction = DownDirection(self.xs, 0)

    def execute(self) -> List[int]:
        result = []
        while self.xs:
            res = self.direction.execute()
            result.extend(res)
            self.direction = self.direction.next()
        return result

    def append_row(self, row: List[str]):
        self.xs.append(deque(row))


async def get_matrix(url: str) -> List[int]:
    response: httpx.Response = await get_text_by_url(url)
    assert response.status_code == CODE_OK, response.text
    rows = response.text.split("\n")
    alg = Algorithm()
    # Только в каждой второй строчке начиная с первой и до предпоследней есть значения
    for row in rows[1:-1:2]:
        alg.append_row(get_elements(row))
    return alg.execute()
