import pytest
from add import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 2) == 1
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0
