from math import floor

def binarySearch(arr: list, target: int):
    leftBound = 0
    rightBound = len(arr) - 1

    while leftBound <= rightBound:
        midPoint = floor((leftBound + rightBound) / 2)

        if arr[midPoint] == target:
            return midPoint

        if arr[midPoint] < target:
            leftBound = midPoint + 1
        else:
            rightBound = midPoint - 1

    return -1

