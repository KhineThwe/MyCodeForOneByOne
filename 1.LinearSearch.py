#Linear Search
#data = 20 30 40 50 60 70 80
#key =60
#Liear Search သည် ထိပ်ဆုံးနေရာကနေသွားရှာတယ်
#if key == arr[i] return arr[i]
#data မတွေ့မချင်းရှာတာဖြစ်တဲ့အတွက် အချိန်ပိုကြာတယ်
#LinearSearch(array, key)
  # for each item in the array
  #   if item == value
  #     return its index
def linear_search(array,n,x):
    for i in range(0,n):
        if(array[i] == x):
            return i
    return -1

if __name__ == "__main__":
    nums = [2,5,10,11,15,16,17,19,25,30,40]
    key = 0
    n = len(nums)
    find_no =  int(input("Please enter a number to find: "))
    result = linear_search(nums,n,find_no)
    #parameter အနေနဲ့ရှာချင်တဲ့ array,size,key
    if result == -1:
        print("Element not found")
    else:
        print("Element found at index: ",result)

