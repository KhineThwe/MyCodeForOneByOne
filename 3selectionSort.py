#selection sort
#1. Set the first element as minimum
#20 12 10 15 2 ---> 20 assume smallest element
#2.Compare minimum with the second element.
# If the second element is smaller than minimum, assign the second element as minimum.
#After each iteration, minimum is placed in the front of the unsorted list.


def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [20, 12, 10, 15, 2]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
