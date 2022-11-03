# #parameterDefault.py
#
# def bShop(name,quantity,unit,tList=[]):
#     tList.append('{0} {1} {2}'.format(name,quantity,unit))
#     return tList
#
# store1 = bShop("Java",1,"Book")
# bShop('python',2,'book',store1)
# store2 = bShop('c++',3,'book')
# print(store1)
# print(store2)
# #['Java 1 Book', 'python 2 book', 'c++ 3 book']
# #['Java 1 Book', 'python 2 book', 'c++ 3 book']
# #ka parameter default problem
# #စစ်ကြည့်လို့ရတယ် is ---> memory address same
# #အရင်ခေါ်ထားတဲ့ memory address ko မှတ်ထားပြီး အဲ့မှာပဲ data သွား store တဲ့ပြသနာ ဖြစ်တယ်
# if store1 is store2:
#     print('They are same')
#ver1


def bShop(name,quantity,unit,tList=None):
    if not tList:#tList ထဲမှာ ဘာမှမရှိဘူးဆိုမှ list အလွတ် တစ်ခုဖန်တီးမယ်
        tList = []
    tList.append('{0} {1} {2}'.format(name, quantity, unit))
    return tList
# store1 = bShop("Java",1,"Book")
# bShop('python',2,'book',store1)
# store2 = bShop('c++',3,'book')
# store3 = bShop('Javascript',4,'book')
# bShop('assembly',5,'book',store3)
# print(store1)
# #['Java 1 Book', 'python 2 book']
# print(store2)
# #['c++ 3 book']
# print(store3)
# #['Javascript 4 book', 'assembly 5 book']
# if store1 is store2:
#     print('They are same')
# else:
#     print('They are not same')
#ver2

#ver3
store1 = bShop("Java",1,"Book")
bShop('python',2,'book',store1)
store2 = bShop('c++',3,'book')
bShop('Javascript',4,'book',store2)
bShop('assembly',5,'book',store2)
print(store1)
# ['Java 1 Book', 'python 2 book']
print(store2)
# ['c++ 3 book', 'Javascript 4 book', 'assembly 5 book']
if store1 is store2:
    print('They are same')
else:
    print('They are not same')

