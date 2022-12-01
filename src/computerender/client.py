"""computerender."""
import os
from typing import Any
from typing import Optional

import aiohttp
from aiohttp import FormData


class Computerender:
    """Client for the computerender API."""

    api_key: str
    base_url = "https://api.computerender.com"

    def __init__(self, api_key: Optional[str] = None) -> None:
        """Initialize api client."""
        self.api_key = api_key or os.environ["CR_KEY"]

    async def generate(self, prompt: str, **kwargs: Any) -> bytes:
        """Generate an image."""
        route = "/generate"
        form_data = FormData(kwargs)
        form_data.add_field("prompt", prompt)
        async with aiohttp.ClientSession(self.base_url) as session:
            resp = await session.post(
                route,
                data=form_data,
                headers={"Authorization": f"X-API-Key {self.api_key}"},
            )
            if resp.status != 200:
                print(await resp.text())
            return await resp.read()
