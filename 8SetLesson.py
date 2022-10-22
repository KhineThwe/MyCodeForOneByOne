#Set -------> unordered--->index နဲ့ထုတ်လို့မရ
my_set_list = {1,2,3,'Hello',(1,2,3)}
print(my_set_list)

#set cannot have duplicates data
my_set_list1 = {1,2,3,4,3,5}
print(my_set_list1)

my_tuple_1 = (1,2,3,4,4)
print(list(my_tuple_1))
print(type(my_tuple_1))


my_set = set([1,2,3,4])
print(my_set)
print(type(my_set))

#Set ထဲမှာ list ထည့်လို့မရ tuple ထည့်လို့ရ
# my_set1 = {1,2,[3,4]} #Error
my_set1 = {1,2,(3,4)}
print(my_set1)
