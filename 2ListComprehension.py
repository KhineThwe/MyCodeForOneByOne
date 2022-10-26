#List comprehension 2
numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12]
# new_list =[num for num in numbers if num % 2 == 0]

#nested condition
new_list =[num for num in numbers if num % 2 == 0 if num %3 == 0]

#if else in list comprehension
new_list1 =[num*2 if num % 2 == 0 else num for num in numbers]
#odd number will return same but even will double

print (new_list)
print(new_list1)


students = ["Bo Bo","Aye Min","Min Min","Aye Myat","Ko Aung","Aung Aung"]
new_name_list = [name for name in students if name[0]=='A']
print(new_name_list)
