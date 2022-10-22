#Dif between List & Tuple
#List ---> can change(item assignment)
#Tuple ---> cannot change
my_tuple = (1,2,3,'Khine',(3,4,5))
# my_tuple[1] = 22222 #Error
print(my_tuple)

#concatenation
my_tuple2=('NCC','Python')
my_total_tuple = my_tuple + my_tuple2
print(my_total_tuple)

print(("NCC",)*3)

#To Delete Tuple
#Can't delete items
#Can delete an entire tuple
del my_tuple
