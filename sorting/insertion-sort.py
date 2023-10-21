def insertionSort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        
        # insert key into sorted sub array data[1:i - 1]
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    print(data)

insertionSort([5, 2, 4, 6, 1, 3])
