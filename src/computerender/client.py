"""computerender."""
from typing import Optional, Dict, Any
import aiohttp
from aiohttp import FormData
import os
from urllib.parse import quote_plus

class Computerender:
    """Client for the computerender API."""

    api_key: str
    base_url = "https://api.computerender.com"

    def __init__(self, api_key: Optional[str] = None) -> None:
        """Initialize api client."""
        self.api_key = api_key or os.environ["CR_KEY"]

    async def generate(self, prompt: str, **kwargs: Dict[str, Any]) -> bytes:
        """Generate an image."""
        method = "generate/"
        form_data = FormData(kwargs)
        async with aiohttp.ClientSession.request() as session:
            result = await session.post(
                self.base_url + method,
                data=form_data,
                headers={"Authorization": f"X-API-Key {self.api_key}"}
            )
            return result

    def do_it(self) -> None:
        """Test method that does nothing."""
        print("oh baby a triple")
