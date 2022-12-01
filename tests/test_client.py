"""Test cases for the client module."""
import io

import pytest
from PIL import Image

from computerender import Computerender


def test_client_succeeds_no_key() -> None:
    """Client can be initialized with no arg."""
    cr_client = Computerender()
    assert cr_client is not None


def test_client_succeeds_w_key() -> None:
    """Client can be initialized with key arg."""
    cr_client = Computerender("test")
    assert cr_client.api_key == "test"


@pytest.mark.asyncio
async def test_client_generate_basic() -> None:
    """Client returns data on generate."""
    cr_client = Computerender()
    result = await cr_client.generate("what's up gamers", iterations=20, height=256)
    image = Image.open(io.BytesIO(result))
    assert image.width == 512
    assert image.height == 256
