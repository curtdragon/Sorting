# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ) :
    # loop through n-1 elements
    for i in range(0, len(arr) - 1) :
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range (i+1, len(arr)) :
            if arr[cur_index] > arr[j] :
                cur_index = j

        # TO-DO: swap
        smallest_index = arr[i]
        arr[i] = arr[cur_index]
        arr[cur_index] = smallest_index

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1) :
            if arr[j] > arr[j+1] :
                hold = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = hold

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr