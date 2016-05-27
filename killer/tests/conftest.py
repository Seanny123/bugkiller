import pytest

print("reading conftest.py in the subfolder")

@pytest.fixture
def thing():
   return "socks"