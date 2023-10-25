from math import floor

def merge_sort(arr):
    if len(arr) > 1:
        midPoint = floor(len(arr)/2)
        leftArr = [element for element in arr[:midPoint]]
        rightArr = [element for element in arr[midPoint:]]

        print('!', leftArr, rightArr)

        if len(leftArr) == 1 and len(rightArr) > 1:
            
        if len(rightArr) == 1 and len():
        merge_sort(leftArr)
        merge_sort(rightArr)


merge_sort([1,4,1,2,5,1])