import asyncio
import requests
from typing import Any

JSON_Response = dict[str, Any]

def get_http_sync(url: str) -> JSON_Response:
    response = requests.get(url)
    return response.json()

async def get_http(url: str) -> JSON_Response:
    return await asyncio.to_thread(get_http_sync, url)