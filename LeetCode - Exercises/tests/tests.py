import pytest
from ..plus_one import plusone

def test_plus_one():
    assert [1,2,5] == plusone([1,2,4])
    assert [1,0,0,0] == plusone([9,9,9])