import pytest
from ..app import main

class TestClass:
  def test_hello_world(self):
    """
      Hello test
    """
    
    assert main.hello_world() == {"Hello": "World"}  # it should return hello world 
