import pytest
from binary_search import binarySearch

@pytest.fixture
def numArray():
    return list([1,2,3,4,5,6,7])

@pytest.fixture
def target():
    return int(5)

def test_binary_search(numArray, target):
    result = binarySearch(numArray, target)
    assert result == 4

def test_binary_search_existing_target(numArray, target):
    result = binarySearch(numArray, target)
    assert result == 4

def test_binary_search_non_existing_target(numArray):
    result = binarySearch(numArray, 8)  # Target not in the list
    assert result == -1

def test_binary_search_empty_list():
    result = binarySearch([], 5)  # Empty list
    assert result == -1

def test_binary_search_target_at_beginning(numArray):
    result = binarySearch(numArray, 1)  # Target is at the beginning
    assert result == 0

def test_binary_search_target_at_end(numArray):
    result = binarySearch(numArray, 7)  # Target is at the end
    assert result == 6