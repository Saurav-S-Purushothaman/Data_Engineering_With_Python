import pandas as pd
import json


# binary search

# Assume that the list is ordered
# go to the middle of the list
# see if the middle value is equal to input 
# if yes return true and the index = middle_value
# if not true
# compare if the middle value is greater than input
# if true, then do the same for the right side value of the array. That is the value from middle index to the end index.
# if false, then do the same for the left side value of the array. That is the value from middle index to the start index.


def binary_search(arr,n):
    left_bound = 0
    right_bound = len(arr)-1
    
    while left_bound <= right_bound:
        mid_index = int((left_bound + right_bound) // 2)
        if arr[mid_index] == n:
            return mid_index
        elif arr[mid_index] < n: 
            left_bound = mid_index+1 
        else:
            right_bound = mid_index-1
    return -1 


if __name__ == "__main__":
    arr = [1,2,3,4,5,12,21,32,32,3,23,2,32,32,3,23,2,32,32,3,2,32,3,2,32,3,2,32,3,2,32,3,2,32,3,2,32,3,2,32,3,23,2,3,2,434,34,3,43,43,43,4,34,34,3,43,4,34,3,43,4,34,34,3,4,34,34,34,3,43]
    arr.sort()
    n = 5
    x = binary_search(arr,n)
    print(x)
