colors = ["Red","Green","Yellow","Blue"]

print('*'.join(colors))
text = ",".join(colors)
print(text)

#List comprehension
# mystr = "Hello"
# mylist = []

# for c in mystr:
#     mylist.append(c)

# print(mylist)
#Loop pat sa yar ma lo pl a myan te sout nee

mystr = "Hello"
mylist = [c.upper() for c in mystr]
#list htl pyan hte mhar ll c

print(mylist)

numbers = [1,2,3,4,5]
mylist1 = [num*2 for num in numbers]
print(mylist1)


