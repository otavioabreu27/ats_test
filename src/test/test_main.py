"""Test Module for the main.py module."""
from ..app import main


class TestClass:
    """Main Module test class."""

    def test_hello_world(self):
        """Hello test."""
        assert main.hello_world() == {"Hello": "World"}
