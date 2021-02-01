# Initializes all the variables from a array input
def start_sort(array):
    quicksort(array, 0, (len(array) - 1))


# Does the sorting via recursion. Ideally in an expedient manner
def quicksort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
        p = partition(array, low, high)
        quicksort(array, low, p - 1)
        quicksort(array, p + 1, high)


# Partitions the arrays. The pivot is just set to the last value this time
# since the average of three implementation was scuffed
def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


if __name__ == '__main__':
    sample = [1, 5, 2, 55, 2, 12, 2, 1, 3]
    start_sort(sample)
    print(sample)
