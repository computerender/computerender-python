"""Test cases for the client module."""
from computerender import Computerender


def test_client_succeeds_no_key() -> None:
    """Client can be initialized with no arg."""
    cr_client = Computerender()
    assert cr_client is not None


def test_client_succeeds_w_key() -> None:
    """Client can be initialized with key arg."""
    cr_client = Computerender("test")
    assert cr_client is not None


def test_client_succeeds_test() -> None:
    """Client can be initialized and test method called."""
    cr_client = Computerender()
    cr_client.do_it()
    assert cr_client is not None