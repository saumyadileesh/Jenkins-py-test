import pytest
from add import add

def test_add():
    assert add(2, 4) == 6
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0
