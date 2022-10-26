#Dictionary Comprehension

my_dictionary = {"first":1,"second":2,"third":3}

# new_dictionary = {k:v*2 for k,v in my_dictionary.items()}

new_dictionary = {k.upper():v*2 for k,v in my_dictionary.items()}

print(new_dictionary)


#List to dictionary Comprehension
my_new_list = [1,2,3,4,5]
new_dictionary1 = {num:num*2 for num in my_new_list}
print(new_dictionary1)

#even odd
# new_dictionary2 = {num:"even" for num in my_new_list}
new_dictionary2 = {num:("even" if num % 2 == 0 else "odd") for num in my_new_list}
print(new_dictionary2)
