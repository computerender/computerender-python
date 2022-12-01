"""computerender."""
import os
from typing import Any
from typing import Dict
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

    async def generate(self, prompt: str, **kwargs: Dict[str, Any]) -> bytes:
        """Generate an image."""
        route = "/generate"
        form_data = FormData(kwargs)
        async with aiohttp.ClientSession(self.base_url) as session:
            result = await session.post(
                route,
                data=form_data,
                headers={"Authorization": f"X-API-Key {self.api_key}"},
            )
            return await result.read()
