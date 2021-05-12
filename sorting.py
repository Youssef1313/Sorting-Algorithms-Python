def quick_sort_helper(arr, s, e):
    if e - s <= 0:
        return

    bound = e + 1
    for i in range(e, s, -1):
        if arr[s] - arr[i] < 0:
            bound -= 1
            arr[bound], arr[i] = arr[i], arr[bound]

    bound -= 1
    arr[bound], arr[s] = arr[s], arr[bound]
    quick_sort_helper(arr, s, bound - 1)
    quick_sort_helper(arr, bound + 1, e)


def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)


def selection_sort(arr):
    for i in range(0, len(arr), 1):
        min_element = i
        for j in range(i, len(arr), 1):
            if arr[min_element] > arr[j]:
                min_element = j

        arr[i], arr[min_element] = arr[min_element], arr[i]


def merge_sort(arr):
    length = len(arr)
    mid = length // 2
    if length > 1:
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(arr, left, right)


def merge(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def heap_sort(arr):
    length=len(arr)
    for i in range (length//2 -1,-1,-1):
        heapify(arr,length,i)

    for i in range (length-1,0,-1):
        arr[0] , arr[i] = arr[i] , arr[0]
        heapify(arr,i,0)


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)