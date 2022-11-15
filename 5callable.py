#callable ဆိုတာ python ရဲ့ built in fun,class,method
#call loe ya yin True ma ya yin Fasle return pyan pay tal
#callable
#print len callable str.upper list.append
#userdefined function,lambda ---> callable
#not object are not callable
print(callable(print))
print(callable('xyz'.upper))
print(callable(callable))

test = print('hello')
print(test)

al = [1,2,3,4]
result = al.append(5)
print(al)
print(result)

from decimal import Decimal
print(callable(Decimal))
a = Decimal('10.10')
print(type(a))
print(callable(a))
