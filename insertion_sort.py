def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Test the function
data = [5, 3, 4, 2, 8]
print("Original:", data)
print("Sorted (Descending):", insertion_sort_desc(data))
