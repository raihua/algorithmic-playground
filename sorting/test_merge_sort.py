import pytest
from merge_sort import merge_sort

@pytest.fixture
def arr():
    return [1,4,1,2,5,1]

def test_merge_sort(arr):
    result = merge_sort(arr)
    assert result == [1,1,1,2,4,5]

    