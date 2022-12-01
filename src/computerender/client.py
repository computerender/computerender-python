"""computerender."""


class Computerender:
    """Client for the computerender API."""

    api_key: str

    def __init__(self, api_key: str = "bad") -> None:
        """Initialize api client."""
        self.api_key = api_key

    def do_it(self) -> None:
        """Test method that does nothing."""
        print("oh baby a triple")
