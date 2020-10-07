# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start <= end:
        middle_index = (start + end) // 2
        if arr[middle_index] == target:
            return middle_index
        elif arr[middle_index] > target:
            return binary_search(arr, target, start, middle_index)
        elif arr[middle_index] < target:
            return binary_search(arr, target, middle_index, end)
    else:    
        return -1

'''
# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    def ascending_binary_search(arr, target, start, end):
        if start <= end:
            middle_index = (start + end) // 2
            if arr[middle_index] == target:
                return middle_index
            elif arr[middle_index] > target:
                return ascending_binary_search(arr, target, start, middle_index)
            elif arr[middle_index] < target:
                return ascending_binary_search(arr, target, middle_index, end)
        else:    
            return -1

    def descending_binary_search(arr, target, start, end):
        if start <= end:
            middle_index = (start + end) // 2
            if arr[middle_index] == target:
                return middle_index
            elif arr[middle_index] < target:
                return descending_binary_search(arr, target, start, middle_index)
            elif arr[middle_index] > target:
                return descending_binary_search(arr, target, middle_index, end)
        else:    
            return -1
    
    if arr[0] < arr[-1]:        
        return ascending_binary_search(arr, target, 0, len(arr)-1)
    else:
        return descending_binary_search(arr, target, 0, len(arr)-1)
'''