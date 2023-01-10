"""computerender."""
import os
from typing import Any
from typing import Optional

import aiohttp
from aiohttp import FormData


class InvalidAuthError(Exception):
    """Auth Invalid."""

    pass


class UnsafePromptError(Exception):
    """Potentially unsafe words in prompt."""

    pass


class UnrecognizedParameterError(Exception):
    """Unrecognized parameter in request."""

    pass


class InvalidParameterError(Exception):
    """Invalid parameter in request."""

    pass


class InternalError(Exception):
    """Internal Server Error."""

    pass


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
        form_data = FormData()
        form_data.add_field("prompt", str(prompt))
        for key, val in kwargs.items():
            form_data.add_field(key, val if type(val) == bytes else str(val))
        async with aiohttp.ClientSession(self.base_url) as session:
            resp = await session.post(
                route,
                data=form_data,
                headers={"Authorization": f"X-API-Key {self.api_key}"},
            )
            if resp.status != 200:
                error_info = await resp.json()
                err_type = error_info["errorType"]
                if err_type == "INVALID_AUTH":
                    raise InvalidAuthError(error_info)
                elif err_type == "UNSAFE_PROMPT":
                    raise UnsafePromptError(error_info)
                elif err_type == "UNRECOGNIZED_PARAMETER":
                    raise UnrecognizedParameterError(error_info)
                elif err_type == "INVALID_PARAMETER":
                    raise InvalidParameterError(error_info)
                elif err_type == "INTERNAL_ERROR":
                    raise InternalError(error_info)
                else:
                    raise Exception(error_info)

            return await resp.read()
