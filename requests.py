import httpx


async def get_text_by_url(url: str) -> httpx.Response:
    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.get(url)
        return response
