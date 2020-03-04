# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    i = 0
    j = 0
    k = 0

    while i < n1 and j < n2:
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            k = k + 1
            i = i + 1
        else:
            merged_arr[k] = arrB[j]
            k = k + 1
            j = j + 1

    while i < n1:
        merged_arr[k] = arrA[i]
        k = k + 1
        i = i + 1

    while j < n2:
        nerged_arr[k] = arrB[j]
        k = k + 1
        j = j + 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i = i+1
            else:
                arr[k] = right[j]
                j = j+1
            k = k+1

        while i < len(left):
            arr[k] = left[i]
            i = i+1
            k = k+1

        while j < len(right):
            arr[k] = right[j]
            j = j+1
            k = k+1

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
