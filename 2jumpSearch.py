#Jump search like binary search for sorted arrays
#The increasing order of performance is:
# linear search  <  jump search  <  binary search
import math
def jump_search(array,n,x):
    #Finding block size to be jumped
    step = math.sqrt(n)

    # Finding the block where element is
    # present (if it is present)
    prev = 0
    while array[int(min(step,n)-1)] < x:
        prev = step#prev = 4
        step += math.sqrt(n)
        if prev >= n:
            return -1

    # Doing a linear search for x in
    # block beginning with prev.
    while array[int(prev)] < x:
        prev += 1

        # If we reached next block or end
        # of array, element is not present.
        if prev == min(step, n):
            return -1

        # If element is found
    if array[int(prev)] == x:
        return prev
    return -1


if __name__ == "__main__":
    nums = [0, 1, 1, 2, 3, 5, 8, 13, 21,
           34, 55, 89, 144, 233, 377, 610]
    key = 0
    n = len(nums)
    find_no =  int(input("Please enter a number to find: "))
    result = jump_search(nums,n,find_no)
    #parameter အနေနဲ့ရှာချင်တဲ့ array,size,key
    if result == -1:
        print("Element not found")
    else:
        print("Number" , find_no, "is at index" ,"%.0f"%result)


