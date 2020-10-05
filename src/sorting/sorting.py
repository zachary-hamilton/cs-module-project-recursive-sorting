import random

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    a_index = 0
    b_index = 0
    merged_index = 0

    # this will compare and add the smaller value in A nd B and then move to next of that list
    while a_index < len(arrA) and b_index < len(arrB): # this while loop will end when one list is fully used
        if arrA[a_index] < arrB[b_index]:
            merged_arr[merged_index] = arrA[a_index]
            a_index += 1
        else:
            merged_arr[merged_index] = arrB[b_index]
            b_index += 1
        merged_index += 1

    # one of the two arrays will still have values so these while loops will add them in
    while a_index < len(arrA):
        merged_arr[merged_index] = arrA[a_index]
        a_index += 1
        merged_index += 1

    while b_index < len(arrB):
        merged_arr[merged_index] = arrB[b_index]
        b_index += 1
        merged_index += 1


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        return merge(merge_sort(left), merge_sort(right))
    else:
        return arr


    
'''
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here
'''
'''
woo = random.sample(range(6000), 5000)
print(merge_sort(woo))
'''
