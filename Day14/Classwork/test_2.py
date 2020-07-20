import pytest
from func2 import validate_args

def test_func2():
    assert validate_args(3, int)