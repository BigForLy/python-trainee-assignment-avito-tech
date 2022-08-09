import httpx


async def get_text_by_url(url: str) -> str:
    async with httpx.AsyncClient() as client:
        try:
            response: httpx.Response = await client.get(url)
            response.raise_for_status()
            return response.text
        except httpx.RequestError as exc:
            print(f"An error occurred while requesting {exc.request.url!r}.")
            return ""
        except httpx.HTTPStatusError as exc:
            print(
                f"Error response {exc.response.status_code} while requesting {exc.request.url!r}."
            )
            return ""
