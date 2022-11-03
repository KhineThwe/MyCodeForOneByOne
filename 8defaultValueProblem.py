#default value problem
#datetime တွေကို သုံးတဲ့အချိန်မှာ current time တွေကိုမပေးဘဲနဲ့ဖြစ်နေတယ်ဆိုရင် ဒီလိုမျိုးဖြေရှင်းရမယ်။
#အရင် PROGRAM မှာ run ထားတဲ့ value တွေသာထပ်ခါထပ်ခါပြနေတာ ကို default value ဝင်တယ်လို့ ပြောတတ်တယ်
from datetime import datetime

# time = datetime.utcnow()
# print("Current Time",time)

# def myFun(msg,*,dt=datetime.utcnow()):
#     print("{0}:{1}".format(dt,msg))
#
# myFun('Text message')
#ver1
#ver2
#ကျွန်တော်တို့ project ရေးတဲ့အခါမှာ funcall ကနေ default value တွေပဲဝင်နေတယ်ဆိုရင်
def myFun(msg,*,dt=None):
    if not dt:#dt == null phyit mha
        dt = datetime.utcnow()
        print('{0}:{1}'.format(dt,msg))
myFun('Text message')
