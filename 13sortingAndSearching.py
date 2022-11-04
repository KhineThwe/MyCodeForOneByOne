# https://technologystrive.com/bubble-sort/
# Bubble Sort in python
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):  #
            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


def binarySearch(array, x, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


if __name__ == '__main__':
    data = [-2, 45, 0, 11, -9]
    bubbleSort(data)
    print('Sorted Array in Ascending Order: ')
    print(data)
    toFind = -2
    result = binarySearch(data, toFind, 0, len(data) - 1)

    if result != -1:
        print("Element is present at index " + str(result))
    else:
        print("Not found")
