"""Test cases for the client module."""
from computerender import Computerender
import pytest

def test_client_succeeds_no_key() -> None:
    """Client can be initialized with no arg."""
    cr_client = Computerender()
    assert cr_client is not None


def test_client_succeeds_w_key() -> None:
    """Client can be initialized with key arg."""
    cr_client = Computerender("test")
    assert cr_client.api_key == "test"


def test_client_succeeds_test() -> None:
    """Client can be initialized and test method called."""
    cr_client = Computerender()
    cr_client.do_it()
    assert cr_client is not None

@pytest.mark.asyncio
async def test_client_generate_basic() -> None:
    """Client returns data on generate"""
    cr_client = Computerender()
    result = await cr_client.generate("what's up gamers", iterations=20)
    assert result is not None