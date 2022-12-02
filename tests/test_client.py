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
    result = await cr_client.generate("what's up gamers")
    image = Image.open(io.BytesIO(result))
    assert image.width == 512
    assert image.height == 512


@pytest.mark.asyncio
async def test_client_generate_error() -> None:
    """Client throws error on bad request."""
    with pytest.raises(Exception):
        cr_client = Computerender()
        await cr_client.generate("what's up gamers", w=9000)


@pytest.mark.asyncio
async def test_client_generate_kwargs() -> None:
    """Client returns data on generate."""
    cr_client = Computerender()
    result = await cr_client.generate("what's up gamers", iterations=20, h=256)
    image = Image.open(io.BytesIO(result))
    assert image.width == 512
    assert image.height == 256


@pytest.mark.asyncio
async def test_client_generate_img2img() -> None:
    """Client does img2img."""
    cr_client = Computerender()
    input_img = Image.new(mode="RGB", size=(384, 384))
    img_buf = io.BytesIO()
    input_img.save(img_buf, format="JPEG")
    img_bytes = img_buf.getvalue()
    result = await cr_client.generate("what's up gamers", iterations=20, img=img_bytes)
    image = Image.open(io.BytesIO(result))
    assert image.width == 384
    assert image.height == 384
