#raise
# try:
#     a = 10/0
# except ZeroDivisionError as err:
#     print(err)
#ZeroDivisionError class ထဲမှာရေးထားတဲ့ စာသားထွက်လာခြင်းဖြစ်တယ်
#ကိုယ်ပိုင် exception ဖန်တီးချင်တယ်ဆိုရင် python မှာခွင့်ပြုပေးထားတယ် ဖန်တီးမယ်ဆိုရင် base class ဖြစ်တဲ့ Exception class ကို inheritance လုပ်ပြီးမှ လုပ်လို့ရမယ်

class myExcept(Exception):
    # print("This is from my Exception")
    pass
class nameError(Exception):
    # print("This is from name error")
    pass
class valueError(Exception):
    # print("This is from value error")
    pass

try:
    a = 10
    b = 20
    if a is b:
        raise valueError
    else:
        raise nameError
except nameError:
    print("Name error")
except valueError:
    print("Value error")

