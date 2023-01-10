"""Test cases for the client module."""
import io

import pytest
from PIL import Image

from computerender import Computerender
from computerender import InvalidAuthError
from computerender import InvalidParameterError
from computerender import UnrecognizedParameterError
from computerender import UnsafePromptError


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
    result = await cr_client.generate("test prompt")
    image = Image.open(io.BytesIO(result))
    assert image.width == 512
    assert image.height == 512


@pytest.mark.asyncio
async def test_client_generate_kwargs() -> None:
    """Client returns data on generate."""
    cr_client = Computerender()
    result = await cr_client.generate("test prompt", iterations=20, h=256)
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
    result = await cr_client.generate("test prompt", iterations=20, img=img_bytes)
    image = Image.open(io.BytesIO(result))
    assert image.width == 384
    assert image.height == 384


@pytest.mark.asyncio
async def test_client_throws_invalid_auth() -> None:
    """Client throws invalid auth."""
    with pytest.raises(InvalidAuthError):
        cr_client = Computerender("sk_bad_key")
        await cr_client.generate("test prompt")


@pytest.mark.asyncio
async def test_client_throws_unsafe_prompt() -> None:
    """Client throws unsafe prompt."""
    with pytest.raises(UnsafePromptError):
        cr_client = Computerender()
        await cr_client.generate("nude")


@pytest.mark.asyncio
async def test_client_throws_unrecognized_parameter() -> None:
    """Client throws unrecognized parameter."""
    with pytest.raises(UnrecognizedParameterError):
        cr_client = Computerender()
        await cr_client.generate("test prompt", bad_param=99)


@pytest.mark.asyncio
async def test_client_throws_invalid_parameter() -> None:
    """Client throws invalid parameter."""
    with pytest.raises(InvalidParameterError):
        cr_client = Computerender()
        await cr_client.generate("test prompt", h=4096)


@pytest.mark.asyncio
async def test_client_throws_dims_small() -> None:
    """Client throws dims too small."""
    with pytest.raises(InvalidParameterError):
        cr_client = Computerender()
        await cr_client.generate("test prompt", w=64)
