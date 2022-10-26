#extended unpacking


#1.list unpacking
a,*b = [1,2,3,4,5,56]
#we have to use *
#we can use * in both sides,right and left
#this one is ok in list and tuple but not ok in dictionary
#in dictionary we have to use double **
print(a)#return first element only
print(type(b))#return others in as a list 


#2.tuple unpacking
a,*b= (1,2,3,4,5,6)
print(a)
print(type(b))


#3.string extended unpacking
#we cannot use * 2 ku
a,*b,c = 'nccpython'
print(a)
print(b)
print(c)


#4.extended unpacking in righthand-side
l1 = [1,2,3,4]
l2 = [5,6,7,8]
list = [l1,l2]
print(list)
#it will return nested list

list1 = [*l1,*l2]
print(type(list1))
