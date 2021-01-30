
# Starts the sort
def quicksort(array):
    quicksort_2(array, 0, len(array) - 1)


# Splits the list and does the recursive work
def quicksort_2(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quicksort_2(array, low, p - 1)
        quicksort_2(array, p + 1, high)


# Gets the pivot
def pivot(array, low, high):
    mid = (high + low) // 2
    pivotpos = high
    if array[low] < array[mid]:
        if array[mid] < array[high]:
            pivotpos = mid
    elif array[low] < array[high]:
        pivotpos = low
    return pivotpos


# sets the partition and sorts the numbers
def partition(array, low, high):
    pivindex = pivot(array, low, high)
    pivval = array[pivindex]
    array[pivindex], array[low] = array[low], array[pivindex]
    border = low
    for i in range(low, high+1):
        if array[i] < pivval:
            border += 1
            array[i], array[border] = array[border], array[i]
        array[low], array[border] = array[border], array[low]
    return border


if __name__ == '__main__':
    sample = [3, 5, 2, 55, 1, 9, 6]
    quicksort(sample)
    print(sample)