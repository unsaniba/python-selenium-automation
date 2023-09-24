# 1- Selection Sort
def selection_sort_descending(arr: list):
    for i in range(len(arr)):
        max_index = i  # Initialize max_index with the current index i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:  # Compare with > for descending order
                max_index = j  # Update max_index if a larger element is found
        arr[i], arr[max_index] = arr[max_index], arr[i]  # Swap the elements

    return arr

# 2- Bubble Sort

def bubble_sort_descending(arr: list):
    n = len(arr)
    for i in range(n):
        # Flag to check if any swapping is done in this pass
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:  # Compare with < for descending order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap the elements
                swapped = True

        # If no swapping is done in a pass, the array is already sorted
        if not swapped:
            break

    return arr


# 3-Insertion Sort
def insertion_sort_descending(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key > arr[j]:  # Compare with > for descending order
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr
