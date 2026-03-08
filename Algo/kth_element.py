

from math import pi


def kth_element(arr, k, start=0, end=None):
    pos=partition(arr, start, end)
    if pos == k:
        return arr[pos]
    elif pos > k:
        return kth_element(arr,k,start,pos-1)
    return kth_element(arr,k-pos-1,pos+1,end)

def partition(arr, start, end):
    left, right = start, end
    pivot = arr[end]

    while left < right:
        if left < right and arr[left] < pivot:
            left += 1
        if left < right and arr[right] > pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[end], arr[left] = arr[left], arr[end]
    return left
