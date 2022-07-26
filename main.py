from typing import List
from requests import get_text_by_url
import httpx


async def get_matrix(url: str) -> List[int]:
    response: httpx.Response = await get_text_by_url(url)
    assert response.status_code == 200, response.text
    rows = response.text.split('\n')
    for row in rows[1:-1:2]:
        print(await get_elements(row))


async def get_elements(string_with_numbers: str) -> List[str]:
    return (string_with_numbers
            .replace('|', '')
            .split()
            )


if __name__ == '__main__':
    import asyncio
    url = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
    asyncio.run(get_matrix(url))
