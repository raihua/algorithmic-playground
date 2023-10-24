def insertion_sort(arr):
    # Start from the second element because the first element is considered sorted.
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements that are greater than the key to one position ahead of their current position.
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key in its correct position within the sorted part of the array.
        arr[j + 1] = key

    return arr
