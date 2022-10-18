a = [1,2,3,4,5]
b = [1,2,3,4,5]
#list တွေမှာ value တွေတူသော်လည်းပဲ memory location မတူပါ။
print(id(a),id(b))

value = a is b #check identity op ka memory address ko pl check
print(value)

if a==b:#relational op ka value ko check
    print('They are same value')
else:
    print('They are not in same value')
