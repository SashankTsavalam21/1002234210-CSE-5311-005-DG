import random

def find_kth_element(arr, k, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    
    pivot = random.randint(start, end)
    pivot = rearrange(arr, start, end, pivot)
    
    if pivot == k - 1:
        return arr[pivot]
    elif pivot < k - 1:
        return find_kth_element(arr, k, pivot + 1, end)
    else:
        return find_kth_element(arr, k, start, pivot - 1)

def rearrange(arr, start, end, pivot):
    pivot_value = arr[pivot]
    arr[pivot], arr[end] = arr[end], arr[pivot]
    swap_index = start
    
    for i in range(start, end):
        if arr[i] < pivot_value:
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
            swap_index += 1
    
    arr[end], arr[swap_index] = arr[swap_index], arr[end]
    return swap_index

# Input section
arr = list(map(int, input("Input the list of numbers: ").split()))
k = int(input("Enter the rank of the element to find: "))
print(f"The {k}th smallest element is: {find_kth_element(arr, k)}")
