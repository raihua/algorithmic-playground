from insertion_sort import insertion_sort

# import the insertion_sort function here

def test_insertion_sort_empty_list():
    arr = []
    result = insertion_sort(arr)
    assert result == []

def test_insertion_sort_one_element():
    arr = [5]
    result = insertion_sort(arr)
    assert result == [5]

def test_insertion_sort_sorted_list():
    arr = [1, 2, 3, 4, 5]
    result = insertion_sort(arr)
    assert result == [1, 2, 3, 4, 5]

def test_insertion_sort_reverse_sorted_list():
    arr = [5, 4, 3, 2, 1]
    result = insertion_sort(arr)
    assert result == [1, 2, 3, 4, 5]

def test_insertion_sort_random_order_list():
    arr = [3, 1, 4, 5, 2]
    result = insertion_sort(arr)
    assert result == [1, 2, 3, 4, 5]

def test_insertion_sort_duplicate_elements():
    arr = [4, 2, 4, 1, 3, 2, 1]
    result = insertion_sort(arr)
    assert result == [1, 1, 2, 2, 3, 4, 4]
